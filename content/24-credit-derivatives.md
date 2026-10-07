# Ch 24 — Credit Derivatives

**TL;DR:** Contracts that transfer credit risk. The workhorse is the **CDS** (insurance against default). Portfolio products (CDOs) are priced with the **Gaussian copula** and depend heavily on **correlation**.

## Credit default swap (CDS)
- Buyer pays a periodic **spread** s on notional; seller pays (1 − R) × notional if the reference entity defaults (credit event).
- Settlement: physical (deliver bonds) or **cash via auction**.
- Approx: `s ≈ λ (1 − R)`. Exact: equate PV of expected premium payments with PV of expected payoff, using risk-neutral hazard rates.
- **Market quotes** now: standard coupon (100 or 500 bp) + upfront payment.
- **CDS–bond basis** = CDS spread − bond yield spread (should be ~0; deviates in practice).
- Spreads give **implied default probabilities** — a market-based credit indicator.

## Indices & variations
- **CDX NA IG**, **iTraxx Europe:** 125 names each; index spread ≈ average spread.
- **Binary CDS**, **basket CDS** (first-to-default, nth-to-default), **total return swap** (swap total return on a bond for LIBOR + spread), **CDS forwards / options**.

## Collateralised debt obligations (CDOs)
- **Cash CDO:** pool of bonds tranched. **Synthetic CDO:** pool of short CDS positions tranched.
- Tranche defined by **attachment/detachment** points (e.g., 0–3% equity, 3–7%, …).
- **One-factor Gaussian copula:**
```
x_i = a_i F + √(1 − a_i²) Z_i         (F common factor; ρ = a²)
Q(t | F) = N( [N⁻¹(Q(t)) − √ρ F] / √(1 − ρ) )
```
  Conditional on F, defaults independent → binomial → integrate over F.
- **Implied correlation:** compound (per tranche) or **base correlation** (0–X% tranches). Correlation "smile" is the market's way of fitting the model.
- Higher correlation → equity tranche *less* risky, senior tranche *more* risky.
- Alternatives: t-copula, random factor loadings, implied copula, dynamic models.

## Remember
- Junior tranche holders are "long correlation"; senior holders are "short correlation".
