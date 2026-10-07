# Ch 2 — Mechanics of Futures Markets

**TL;DR:** Futures are standardised exchange contracts with daily settlement through margin accounts, which almost eliminates credit risk.

## Core ideas
- **Contract specs:** asset (and quality grade), contract size, delivery place/month, price quotes, daily price limits, position limits.
- **Most positions are closed out** before delivery by taking the opposite trade.
- **Convergence:** as delivery approaches, futures price → spot price (otherwise arbitrage).
- **Margins:**
  - *Initial margin* deposited when you trade.
  - *Daily settlement (marking to market):* gains/losses credited/debited every day.
  - Falls below *maintenance margin* → **margin call**, top back up to the *initial* level (the extra is *variation margin*).
- **Clearing house** is the counterparty to every trade; brokers post margin with it.
- **OTC markets:** now pushed to central counterparties (CCPs); bilateral trades use collateral (CSA agreements).
- **Open interest** = number of contracts outstanding. **Volume** = contracts traded that day.
- **Order types:** market, limit, stop, stop-limit, market-if-touched, etc.
- **Delivery:** the short chooses when/what grade within rules; some contracts are *cash settled* (e.g., stock index).

## Forwards vs futures
| | Forward | Futures |
|---|---|---|
| Trades | OTC, private | Exchange |
| Terms | custom | standard |
| Settlement | at end | daily |
| Credit risk | some | almost none |
| Usually | delivered / cash-settled at end | closed out early |

## Remember
- Futures price ≈ forward price when rates are constant (Ch 5).
- Daily settlement means you may need cash *before* the hedge pays off — liquidity risk (Metallgesellschaft).
