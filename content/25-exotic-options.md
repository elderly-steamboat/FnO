# Ch 25 — Exotic Options

**TL;DR:** Non-standard options made to fit specific needs. Most can be priced with BSM-style formulas, trees, or Monte Carlo.

## Catalogue
| Type | What it is | Note |
|---|---|---|
| **Packages** | combos of vanilla options/forwards | e.g., zero-cost collar (range forward) |
| **Non-standard American** | Bermudan (exercise on set dates), lock-out, varying strike | trees |
| **Gap** | pays S_T − K1 if S_T > K2 | can have negative payoff |
| **Forward start** | ATM option starting later | worth = ATM option today (no div.) |
| **Cliquet** | series of forward starts | |
| **Compound** | option on an option (call on call, etc.) | bivariate normal |
| **Chooser** | choose call or put at time t1 | = call + put package |
| **Barrier** | knock-in / knock-out at level H | in + out = vanilla; cheaper; sensitive near barrier |
| **Binary** | cash-or-nothing (pays Q), asset-or-nothing (pays S) | call = asset-or-nothing − K × cash-or-nothing |
| **Lookback** | payoff uses max/min price over life | floating or fixed strike; expensive |
| **Shout** | lock in intrinsic once | tree |
| **Asian** | payoff uses average price | cheaper, less volatile; Turnbull–Wakeman approx |
| **Exchange** | swap one asset for another: max(U_T − V_T, 0) | Margrabe formula with σ² = σ_U² + σ_V² − 2ρσ_Uσ_V |
| **Rainbow / basket** | multiple underlyings | Monte Carlo |
| **Volatility & variance swaps** | pay realised vs fixed volatility/variance | variance swap replicated by a strip of options (basis of VIX) |

## Static hedging
Replicate the exotic with a portfolio of vanilla options that matches its value on a boundary — e.g., barrier options. Hedge once, no rebalancing.

## Remember
- Path-dependent exotics → Monte Carlo; American-style features → trees/finite differences.
- Delta can be huge near barriers or for binaries near expiry — hard to hedge.
