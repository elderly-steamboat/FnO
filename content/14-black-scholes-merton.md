# Ch 14 — The Black–Scholes–Merton Model

**TL;DR:** Assume GBM, frictionless markets, constant r and σ. A delta-hedged portfolio is riskless → a PDE → closed-form prices for European options.

## Lognormal facts
```
ln S_T ~ N(ln S0 + (μ − σ²/2)T, σ²T)
E[S_T] = S0 e^(μT)
Realised continuous return x ~ N(μ − σ²/2, σ²/T)
```

## Estimating volatility
Daily log returns `u_i = ln(S_i/S_{i−1})`, sample std s; `σ = s/√τ` (τ = 1/252 for trading days). Volatility mostly comes from **trading days**, not calendar days.

## BSM PDE
```
∂f/∂t + r S ∂f/∂S + ½ σ² S² ∂²f/∂S² = r f
```
Holds for *any* derivative on S; payoff = boundary condition.

## Pricing formulas
```
c = S0 N(d1) − K e^(−rT) N(d2)
p = K e^(−rT) N(−d2) − S0 N(−d1)
d1 = [ln(S0/K) + (r + σ²/2)T] / (σ√T)
d2 = d1 − σ√T
```
Interpretation: N(d2) = risk-neutral prob. call is exercised; S0 N(d1) e^(rT) = expected S_T when exercised (risk-neutral).

## Implied volatility
The σ that makes BSM equal the market price. Solved iteratively. VIX = 30-day implied vol on S&P 500.

## Dividends
- European: subtract PV of dividends from S0.
- American calls: check exercise just before each ex-date. **Black's approximation:** max of European prices for expiry at T and just before last ex-dividend date.

## Warrants / dilution
Value warrant as a call on equity with price scaled by N/(N+M).

## Remember
- μ doesn't appear — risk-neutral valuation again.
- Markets trade *volatility*: quotes are often in implied vol, not dollars.
