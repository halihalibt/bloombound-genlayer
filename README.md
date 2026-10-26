# BLOOMBOUND

**Meaning takes root.** A two-player semantic territory game with a living watercolor garden.

[Play](https://halihalibt.github.io/bloombound-genlayer/) · [Rules](RULES.md) · [Contract](contracts/bloombound.py)

Two gardeners receive different themes. A term grows a flower only when it belongs exclusively to its player's theme and adds a new concept. A paper airplane belongs to both the flying and paper gardens, so neither player can occupy it. GenLayer validators independently assess membership in both themes and semantic novelty. Deterministic code handles turns, scores and the finish.

## Play

The no-wallet Practice mode offers prewritten examples and lets one visitor try both sides. Its results are curated, not live AI judgments. On chain mode accepts free-form noun phrases and requires two distinct wallet addresses on Stable Studionet, chain 61999. Use an injected wallet or the optional temporary Studio players, whose signing keys exist only in page memory and disappear on reload. Temporary addresses must never receive funds. The app includes source verification, wallet/network guards, saved transaction recovery, finalized-success checks, signed-intent binding and game-state readback. No automatic retries or appeals are used.

The visual experience includes an original watercolor botanical illustration, translucent procedural flowers, a floating garden, pointer interactions, score-driven growth and default-on gentle piano music. Devices without WebGL receive an interactive SVG garden. A Chinese introduction is available; fixed game rules remain in English.

## Rules

- Three immutable arena pairs; a creator cannot change the themes after joining.
- Alternate turns between two wallet addresses. Rejected, overlapping and uncertain terms consume a turn.
- Only exclusive membership in the current player's theme scores.
- All attempted terms become novelty history. Synonyms, translations and cosmetic variants are excluded by semantic judgment.
- First to five flowers wins. After 24 attempts, higher score wins; equality draws.
- A participant can resign. No host scoring override, payments, prizes or token rewards.

## Development

Node.js 22+ and Python 3.11+.

```sh
npm ci
npm test
python -m unittest discover -s contract-tests -v
npm run build
npm run dev
```

The local Python suite mocks the GenLayer host and model responses. It verifies state and security invariants; it does not prove live validator agreement. `contracts/bloombound.py` pins its Python runtime. The front end uses genlayer-js 1.1.8.

## Verified deployment

Contract: [`0xb7ACCA0e7edE69b8Cb25c444f266909697320ad5`](https://explorer-studio.genlayer.com/address/0xb7ACCA0e7edE69b8Cb25c444f266909697320ad5). Deployment reached FINALIZED / SUCCESS under full consensus. The deployed source matches the complete bundled file byte-for-byte. The application can verify the protocol from finalized chain state without signing. [Deployment receipt](evidence/deployment.json).

The recorded browser-native match completed six FINALIZED / SUCCESS transactions: creation, a distinct second player joining, two ROOTED moves, one TANGLED move and one ECHO. The final snapshot is revision 5, score 1:1. [Live records](EVIDENCE.md) · [Execution extract](evidence/verified-match.json). Select **On chain → Read verified example** to fetch its current finalized state without signing.

## Network and verification

Only Stable Studionet 61999, `https://studio.genlayer.com/api`, is supported. Zero gas price and zero-value writes are required. Injected-wallet keys remain in the wallet; optional temporary-player keys stay in page memory and are never persisted or exported. This repository makes no claim of mainnet deployment, physical-world truth or market exclusivity.

See [DEPLOYMENT.md](DEPLOYMENT.md) for exact deployment and two-player execution steps. A successful local test or visible Practice flower is never counted as a chain receipt.

## Limitations

Meaning can be ambiguous and model judgments may disagree. The validator checks canonical decision labels independently and audits explanations, but consensus is not an objective dictionary. Wallet separation does not prove different human beings. Players can abandon games; resignation exists but there is no turn clock. Creation is limited to 32 gardens per address; each game is bounded to 24 attempted terms. Public state contains wallet addresses and submitted words.

The illustration was generated for this project. Geometry, game code and interactions are original project assets. MIT licensed.

## Music

“A Garden Between Words” is an original 110-second piano miniature with soft arpeggios, a calm melody and subtle room reflections. Music is enabled by default. Browsers that block audible autoplay start it on the first pointer or keyboard interaction. The music control remembers an explicit mute choice. The original composition and renderer are included in `scripts/render-music.py`; optional regeneration requires NumPy, SciPy and ffmpeg. No external music service or paid API is required.
