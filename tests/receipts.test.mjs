import {test} from 'node:test';import assert from 'node:assert/strict';import {execution} from '../src/receipts.js';
const ok={mode:'leader',execution_result:'SUCCESS',result:{status:'return'}};
test('accepted is not finalized',()=>assert.equal(execution({statusName:'ACCEPTED',consensus_data:{leader_receipt:[ok]}}),'pending'));
test('finalized successful leader survives idle validator receipt',()=>assert.equal(execution({statusName:'FINALIZED',consensus_data:{leader_receipt:[ok,{mode:'validator',execution_result:'ERROR'}]}}),'success'));
test('finalized rollback is failed',()=>assert.equal(execution({statusName:'FINALIZED',consensus_data:{leader_receipt:[{...ok,result:{status:'rollback'}}]}}),'failed'));
test('missing execution cannot claim success',()=>assert.equal(execution({statusName:'FINALIZED'}),'unverified'));
test('cancelled never succeeds',()=>assert.equal(execution({statusName:'CANCELED',txExecutionResult:1}),'failed'));
test('SDK return enum is supported',()=>assert.equal(execution({statusName:'FINALIZED',txExecutionResultName:'FINISHED_WITH_RETURN'}),'success'));

test('SDK integer arguments preserve signed numeric types',async()=>{const {asPlain}=await import('../src/receipts.js');assert.deepEqual(asPlain(new Map([['args',['game',1n,'eagle']]])),{args:['game',1,'eagle']});assert.notDeepEqual(asPlain(['game','1','eagle']),['game',1,'eagle']);});
test('unsafe integers remain exact',async()=>{const {asPlain}=await import('../src/receipts.js');assert.equal(asPlain(9007199254740993n),'9007199254740993');});
