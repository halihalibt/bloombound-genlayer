# Stable Studionet execution

Network: chain **61999**, RPC `https://studio.genlayer.com/api`. This game has no payments or prizes. Use normal full consensus, not leader-only execution. No constructor arguments are required.

## Inspect the existing deployment

The canonical contract is `0xb7ACCA0e7edE69b8Cb25c444f266909697320ad5`. Open **On chain → Read verified example** for a read-only inspection. Existing deployment and match receipts are linked in [EVIDENCE.md](EVIDENCE.md); a new deployment is optional.

## Deploy a new instance

Open the app's **On chain** workspace, connect an injected wallet on Stable Studionet (or expand **No wallet extension?** and choose a temporary Studio player), expand **Create a new garden or deploy the canonical contract**, then select **Deploy contract**. Alternatively upload `contracts/bloombound.py` in GenLayer Studio and deploy the complete file with no constructor arguments. The app uses wallet signing or generates temporary players locally; it does not request private-key entry.

After sending, the app tracks consensus automatically with read-only requests. **Transaction status & recovery → Check finality & read back** also checks explicitly. The address is filled only after successful finalized deployment and byte-for-byte source verification. If a hash was submitted but the UI interrupted, attach the exact hash from wallet history to the saved intent; never resubmit an uncertain write.

## Two-player match

1. Wallet A selects `Between sky & paper`, enters slug `first-bloom`, and selects **Create garden**. Wait for FINALIZED / SUCCESS and readback. The game ID is `<lowercase-wallet-A-address>:first-bloom`.
2. Wallet B opens the same app, sets the verified contract address and game ID, connects its own wallet, and selects **Join as gardener B**. Finalize and read back.
3. Wallet A reads the finalized game and plants `eagle` at revision 1. A clear normal result is ROOTED; the actual consensus outcome is authoritative.
4. Wallet B reads and plants `notebook` at the returned revision.
5. Wallet A reads and plants `paper airplane`. Expected rule behavior is TANGLED with no point, subject to actual independent consensus.
6. Wallet B reads and plants `eagle`. Exact repeat must produce ECHO deterministically.
7. Export the game and each execution record. Each successful operation requires FINALIZED, successful execution, exact sender/function/args binding and state readback. A finalized rollback is a failed write, never a scored move.

The local test suite covers rollback boundaries and consensus rejection with mocked hosts. The recorded live match is linked below. A new match needs its own exported receipts; the walkthrough itself is not execution evidence.

## Recorded example

The existing six-transaction match is documented in [EVIDENCE.md](EVIDENCE.md). Use **On chain → Read verified example** to inspect it without signing or creating a new match. Temporary Studio player accounts remain only in the current page; keep the page open while playing. An injected wallet is appropriate when the same seat must be resumed later.
