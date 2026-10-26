# Live game records

Network: Stable Studionet **61999**. [Canonical contract](https://explorer-studio.genlayer.com/address/0xb7ACCA0e7edE69b8Cb25c444f266909697320ad5).

Six browser-frontend writes reached `FINALIZED / SUCCESS` with `MAJORITY_AGREE` under full consensus. Each transaction was bound to its saved sender, recipient, function and complete arguments, then read back from finalized game state. No appeal or automatic write retry was used.

| Event | Transaction | Business result |
|---|---|---|
| Create garden | [0x1fea5b0f…](https://explorer-studio.genlayer.com/tx/0x1fea5b0fccaffe731fcc63f7e7bfeeb766742968bffee6c54d0ccc0ba60b7da4) | WAITING |
| Join as player B | [0xcdcfbb11…](https://explorer-studio.genlayer.com/tx/0xcdcfbb11cde888006ee6427c983191b028a5498f4978c6fd5bcdd7ad714be5ce) | ACTIVE |
| Player A: eagle | [0xff7fe4a0…](https://explorer-studio.genlayer.com/tx/0xff7fe4a06a602b831fb2ebd308effd8e6b73d6300ae7ea5489649da4c6c57d5e) | ROOTED · A +1 |
| Player B: notebook | [0x7d5e02b4…](https://explorer-studio.genlayer.com/tx/0x7d5e02b460b4ea3fdeb904a79ac3b012dd433aaf139ca1ac20257b49593ff2b4) | ROOTED · B +1 |
| Player A: paper airplane | [0x60752fa5…](https://explorer-studio.genlayer.com/tx/0x60752fa5deb5f182c54e42be10e9c87f12b49fc0772c5a6e13b2a0597d256020) | TANGLED · no point |
| Player B: eagle again | [0x9c5dc2b6…](https://explorer-studio.genlayer.com/tx/0x9c5dc2b664fe09f9698f3fddb89ab2215c390aaec1163ae1a1a8d02868883b65) | ECHO · no point |

## Recorded match

- Game ID: `0x3951519df582b98a5278b1ee25b03adf84420631:verified-bloom`
- Arena: `sky-paper`
- Player A: `0x3951519df582b98a5278b1ee25b03adf84420631`
- Player B: `0x21bf2a677895c1ef20a1df8a8dcc06e3f6b23cfa`
- Final observed state: **ACTIVE · revision 5 · score 1:1 · player A's turn**.

The two addresses were separate temporary browser-native signers. This proves distinct wallet seats, not two independent humans or resistance to collusion. Refreshing the page discards temporary signing accounts; this example remains publicly readable.

## Inspect without a wallet

Open [BLOOMBOUND](https://halihalibt.github.io/bloombound-genlayer/), choose **On chain**, then **Read verified example**. The app verifies the deployed source and reads `get_game` using `LATEST_FINAL`. The two flowers, four attempts and score come from that current chain response. Select a history row to inspect the accepted explanation and labels. **Export garden** downloads the loaded record.

The Practice mode is separately labeled and uses curated examples; it is never presented as live consensus.

## Data

- [Verified transaction and game extract](evidence/verified-match.json)
- [Final browser execution export](evidence/frontend-execution.json)
- [Exported finalized garden](evidence/verified-garden.json)
- [Deployment receipt and byte-for-byte source match](evidence/deployment.json)
- [Deployment manifest](public/deployment.json)

Local coverage includes 16 JavaScript tests and 16 mocked-host Python tests. Live evidence covers creation, joining, semantic scoring, semantic overlap, exact repeats, turn progression, saved-intent binding, pending cleanup and exports. Winning, resignation, 24-move resolution and independent-validator rejection are covered locally, not by separate live receipts. The optional injected-wallet path has not been separately exercised in this record set; the tested frontend signer path is the temporary Studio player mode.

Studionet may reset. These files preserve the observed records, not a promise of perpetual network availability.
