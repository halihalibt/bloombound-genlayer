import unittest, types, sys, json, importlib.util
from pathlib import Path
class Map:
    @classmethod
    def __class_getitem__(cls, key): return dict
class Return:
    def __init__(self, v): self.calldata=v
class VM:
    Return=Return
    @staticmethod
    def run_nondet_unsafe(fn, validator):
        value=fn()
        if not validator(Return(value)): raise Exception('VALIDATOR_REJECTED')
        return value
class Host:
    Contract=object
    public=types.SimpleNamespace(view=lambda fn:fn,write=lambda fn:fn)
    message=types.SimpleNamespace(sender_address='0xa')
    vm=VM
    nondet=types.SimpleNamespace(exec_prompt=lambda *a,**k:None)
host=Host(); module=types.ModuleType('genlayer');module.gl=host;module.TreeMap=Map;module.u32=int;sys.modules['genlayer']=module
spec=importlib.util.spec_from_file_location('bloom',Path(__file__).parents[1]/'contracts/bloombound.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
class GameTest(unittest.TestCase):
    def setUp(self):
        host.message.sender_address='0xa';self.c=b.Bloombound();self.c.games={};self.c.created={};self.id=self.c.create_game('test','sky-paper')
        host.message.sender_address='0xb';self.c.join_game(self.id);host.message.sender_address='0xa'
        self.signals={'a':'YES','b':'NO','novel':'YES','reason':'The candidate is a flying object and is not made of paper.'}
        host.nondet.exec_prompt=lambda prompt,**kw: {'valid':True} if prompt.startswith('Check whether') else self.signals
    def game(self): return json.loads(self.c.get_game(self.id))
    def test_creator_cannot_join_own_garden(self):
        new=self.c.create_game('other','sky-paper')
        with self.assertRaisesRegex(Exception,'DISTINCT_PLAYER'):self.c.join_game(new)
    def test_other_wallet_cannot_take_turn(self):
        host.message.sender_address='0xc'
        with self.assertRaisesRegex(Exception,'NOT_YOUR_TURN'):self.c.plant(self.id,1,'cloud')
    def test_stale_revision(self):
        with self.assertRaisesRegex(Exception,'STALE_TURN'):self.c.plant(self.id,0,'cloud')
    def test_admission_rotates_and_scores(self):
        self.c.plant(self.id,1,'cloud');g=self.game();self.assertEqual(g['score'],[1,0]);self.assertEqual(g['turn'],1)
    def test_overlap_does_not_score(self):
        self.signals['b']='YES';self.c.plant(self.id,1,'paper airplane');self.assertEqual(self.game()['history'][0]['result'],'TANGLED')
    def test_synonym_does_not_score(self):
        self.signals['novel']='NO';self.c.plant(self.id,1,'cloud');self.assertEqual(self.game()['score'],[0,0])
    def test_unknown_no_point(self):
        self.signals['a']='UNKNOWN';self.c.plant(self.id,1,'something');self.assertEqual(self.game()['history'][0]['result'],'UNCERTAIN')
    def test_exact_repeat_no_model(self):
        self.c.plant(self.id,1,'cloud');host.message.sender_address='0xb';host.nondet.exec_prompt=lambda *a,**k: (_ for _ in ()).throw(Exception('MODEL_MUST_NOT_RUN'));self.c.plant(self.id,2,'CLOUD');self.assertEqual(self.game()['history'][1]['result'],'ECHO')
    def test_independent_validator_disagreement(self):
        answers=iter([self.signals,{**self.signals,'a':'NO'}]);host.nondet.exec_prompt=lambda *a,**k:next(answers)
        with self.assertRaisesRegex(Exception,'VALIDATOR_REJECTED'):self.c.plant(self.id,1,'cloud')
        self.assertEqual(self.game()['revision'],1)
    def test_reason_audit_rejection(self):
        host.nondet.exec_prompt=lambda prompt,**kw:{'valid':False} if prompt.startswith('Check whether') else self.signals
        with self.assertRaisesRegex(Exception,'VALIDATOR_REJECTED'):self.c.plant(self.id,1,'cloud')
    def test_resign_other_wins(self):
        self.c.resign(self.id,1);self.assertEqual(self.game()['winner'],1)
    def test_resign_outsider_rejected(self):
        host.message.sender_address='0xc'
        with self.assertRaisesRegex(Exception,'PLAYERS_ONLY'):self.c.resign(self.id,1)
    def test_fifth_point_finishes(self):
        g=self.game();g['score']=[4,0];self.c.games[self.id]=b.pack(g);self.c.plant(self.id,1,'cloud');self.assertEqual(self.game()['status'],'FINISHED')
    def test_24_moves_finishes_draw(self):
        g=self.game();g['history']=[{'word':'x'}]*23;self.c.games[self.id]=b.pack(g);self.signals.update(a='NO');self.c.plant(self.id,1,'cloud');self.assertEqual(self.game()['winner'],-1)
    def test_invalid_model_schema_fails_closed(self):
        self.signals['extra']=True
        with self.assertRaisesRegex(Exception,'JUDGMENT_SCHEMA'):self.c.plant(self.id,1,'cloud')
    def test_creation_limit(self):
        self.c.created['0xa']=32
        with self.assertRaisesRegex(Exception,'CREATION_LIMIT'):self.c.create_game('capped','sky-paper')
if __name__=='__main__': unittest.main()
