# Game rules and trust model

BLOOMBOUND is a bounded two-player game, not a content certification service. Each match fixes two themes, two wallet seats and the complete turn history.

## Theme pairs

| Arena | Gardener A | Gardener B |
|---|---|---|
| sky-paper | Things that can fly through the air | Objects made primarily of paper |
| time-sea | Objects used to measure time | Objects used for travel on water |
| music-light | Objects designed to produce musical sounds | Objects designed to emit visible light |

## Consensus and state

The leader returns `a`, `b`, and `novel` as YES, NO or UNKNOWN, plus a concise explanation. Each validator makes its own judgment from the original candidate, themes and attempted-term history. It compares all three labels and separately audits the proposed explanation. It does not accept a leader's proposed label merely because its text sounds plausible. Malformed output fails closed.

The contract then resolves outcomes in this order: non-novel → ECHO; any uncertainty → UNCERTAIN; dual membership → TANGLED; neither membership → OUTSIDE; exclusive opponent membership → OTHER_GARDEN; exclusive own membership → ROOTED. Only ROOTED increments a score. All resolved attempts advance the revision, consume a turn and enter novelty history. A model/consensus failure does not advance state.

Exact repeated strings are deterministically ECHO without a model call. Semantic novelty includes translations, synonyms, singular/plural forms and cosmetic variants. Distinct concrete subtypes may be allowed. Candidate text is untrusted data, not an instruction channel. Theme definitions are immutable contract constants.

An expected revision prevents stale-turn replay. The current sender must own the active seat. Joining requires a distinct address. No administrator can edit the score, change the arena, impersonate a seat or settle a match.

## End states

Five scored terms end a match immediately. The 24th attempt ends it by score, including draws. A player may resign at either active turn, awarding the opponent a win. A waiting creator may close its unjoined match. There is no appeal method or automatic transaction retry.
