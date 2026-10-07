# Ch 21 — Value at Risk

**TL;DR:** VaR = "we're X% sure we won't lose more than V over N days." One number summarising portfolio risk. Two main ways to compute it: historical simulation and the model-building (variance–covariance) approach.

## Definitions
- **VaR(X%, N days):** loss level exceeded with only (100 − X)% probability.
- **Expected shortfall (ES / CVaR):** average loss *given* that VaR is exceeded. Better: coherent (rewards diversification); VaR isn't always.
- Usually compute 1-day VaR; `N-day VaR = 1-day VaR × √N` (if changes are iid normal).
- Basel: 10-day 99% VaR for market risk capital (plus stressed VaR after 2008).

## Historical simulation
- Take last ~500 days of market-variable changes, apply each to today's portfolio, rank losses, read off the percentile.
- Pros: no distribution assumption. Cons: limited by history.
- Improvements: weight recent observations more, volatility scaling, bootstrap, **extreme value theory** for tails.

## Model-building approach
```
Linear portfolio:  ΔP = Σ α_i Δx_i
σ_P² = Σ Σ ρ_ij α_i α_j σ_i σ_j
VaR = σ_P · N^(−1)(X) · √N
```
- Handle bonds via **cash-flow mapping** to standard maturity vertices.
- Options: use delta (linear) or delta–gamma (quadratic) approximation. Gamma makes distribution skewed → use **Cornish–Fisher** expansion.
- **Monte Carlo** simulation: full revaluation, handles non-linearity.
- **Principal components analysis:** few factors (shift, twist, bow) explain most yield-curve moves.

## Validation
- **Back-testing:** count exceptions (days loss > VaR). Kupiec test for too many/too few; check bunching.
- **Stress testing:** extreme but plausible scenarios not in the data.

## Remember
- Diversification benefit = sum of standalone VaRs − portfolio VaR.
- **Marginal / incremental / component VaR** allocate risk to sub-portfolios; components add up to total.
