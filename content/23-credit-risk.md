# Ch 23 — Credit Risk

**TL;DR:** How likely is a company to default and how much will you lose? Estimate default probabilities from **ratings history**, **bond prices**, or **equity prices (Merton)**, then apply to derivative exposures.

## Basics
- **Ratings:** AAA … BBB (investment grade) … BB and below (junk).
- **Recovery rate R:** % of claim recovered on default (bond price just after default). Negatively correlated with default rates.
- **Hazard rate λ (default intensity):** conditional prob. of default per unit time given survival.
```
Survival to t: Q(t) = 1 − e^(−λ̄ t)
```

## Default probabilities from bond spreads
```
λ ≈ s / (1 − R)       (s = bond yield spread over risk-free)
```
- **Real-world** (historical) probabilities are **much lower** than **risk-neutral** (bond-implied) ones — investors demand compensation for systematic default risk, illiquidity, and tail risk.
- Use risk-neutral for pricing, real-world for scenario/regulatory analysis.

## Merton model (equity as a call on firm assets)
```
E0 = V0 N(d1) − D e^(−rT) N(d2)
σ_E E0 = N(d1) σ_V V0
Risk-neutral default prob = N(−d2)
```
Solve two equations for V0, σ_V. Moody's KMV uses a version of this ("distance to default").

## Derivative credit risk
- Expected loss from counterparty = Σ (prob. default in period) × (1 − R) × (expected exposure).
- **CVA** (credit value adjustment, counterparty defaults), **DVA** (own default).
- Mitigants: **netting**, **collateral**, downgrade triggers.
- **Wrong-way risk:** exposure rises when the counterparty is more likely to default.

## Default correlation
- **Gaussian copula** (one-factor): link default times through a common factor.
- **Vasicek / Basel formula** for worst-case default rate:
```
WCDR(T, X) = N( [N⁻¹(PD) + √ρ N⁻¹(X)] / √(1 − ρ) )
Credit VaR ≈ L × (1 − R) × WCDR − expected loss
```
- CreditMetrics: simulate rating migrations.

## Remember
- Spread ≈ hazard × loss-given-default — the most useful back-of-envelope link in credit.
