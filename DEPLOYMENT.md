# Stable Studionet execution

Network: chain **61999**, RPC `https://studio.genlayer.com/api`. This game has no payments or prizes. Use normal full consensus, not leader-only execution. No constructor arguments are required.

## Deploy

Open the app's **On chain** workspace, connect an injected wallet on Stable Studionet, expand **Create a new garden or deploy the canonical contract**, then select **Deploy contract**. Alternatively upload `contracts/bloombound.py` in GenLayer Studio and deploy the complete file with no constructor arguments. Do not paste a private key into the app or a chat.

After sending, expand **Transaction status & recovery** and use **Check finality & read back**. The address is filled only after successful finalized deployment and byte-for-byte source verification. If a hash was submitted but the UI interrupted, attach the exact hash from wallet history to the saved intent; never resubmit an uncertain write.

## Two-player match

1. Wallet A selects `Between sky & paper`, enters slug `first-bloom`, and selects **Create garden**. Wait for FINALIZED / SUCCESS and readback. The game ID is `<lowercase-wallet-A-address>:first-bloom`.
2. Wallet B opens the same app, sets the verified contract address and game ID, connects its own wallet, and selects **Join as gardener B**. Finalize and read back.
3. Wallet A reads the finalized game and plants `eagle` at revision 1. A clear normal result is ROOTED; the actual consensus outcome is authoritative.
4. Wallet B reads and plants `notebook` at the returned revision.
5. Wallet A reads and plants `paper airplane`. Expected rule behavior is TANGLED with no point, subject to actual independent consensus.
6. Wallet B reads and plants `eagle`. Exact repeat must produce ECHO deterministically.
7. Export the game and each execution record. Each successful operation requires FINALIZED, successful execution, exact sender/function/args binding and state readback. A finalized rollback is a failed write, never a scored move.

The local test suite covers rollback boundaries and consensus rejection with mocked hosts. Live receipts, when available, must be separately recorded; none should be inferred from this walkthrough.
