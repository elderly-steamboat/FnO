# Ch 22 — Estimating Volatilities and Correlations

**TL;DR:** Volatility changes over time. Weight recent data more: **EWMA** (simple) or **GARCH(1,1)** (adds mean reversion to a long-run level).

## Setup
`u_i = ln(S_i/S_{i−1})` (≈ % daily change). Assume mean ≈ 0, so variance ≈ average of u².

## Models
```
Simple:   σ_n² = (1/m) Σ u²_{n−i}
EWMA:     σ_n² = λ σ²_{n−1} + (1 − λ) u²_{n−1}        (RiskMetrics λ = 0.94)
GARCH(1,1): σ_n² = ω + α u²_{n−1} + β σ²_{n−1}
   γ = 1 − α − β,  long-run variance V_L = ω / γ   (need α + β < 1)
```
- EWMA = GARCH with ω = 0 (no mean reversion).
- **Estimate parameters by maximum likelihood:** maximise Σ[−ln v_i − u_i²/v_i].
- Check: autocorrelation of u²/σ² should vanish (Ljung–Box).

## Forecasting with GARCH
```
E[σ²_{n+t}] = V_L + (α + β)^t (σ_n² − V_L)
```
Mean reverts at rate a = ln(1/(α+β)). Implied term structure of volatility for option pricing.

## Correlations
```
Covariance EWMA: cov_n = λ cov_{n−1} + (1 − λ) x_{n−1} y_{n−1}
ρ = cov / (σ_x σ_y)
```
Keep matrices **positive semidefinite** — update everything with the same model/λ.

## Remember
- After a volatility spike, GARCH says it will fade back toward V_L; EWMA says it persists.
