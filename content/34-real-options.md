# Ch 34 — Real Options

**TL;DR:** Use option-pricing ideas to value flexibility in real investment projects — to expand, abandon, delay, or switch. Traditional NPV ignores this flexibility and undervalues projects.

## Why NPV falls short
- NPV discounts expected cash flows at a fixed risk-adjusted rate, but flexibility changes risk over time → no single correct discount rate.
- Options thinking: value project in a **risk-neutral world** and discount at r.

## Risk-neutral approach for non-traded variables
- For a variable θ (e.g., sales volume) with market price of risk λ:
```
Risk-neutral growth = real-world growth − λ σ
λ = ρ (μ_m − r) / σ_m      (CAPM link, ρ = corr. with market)
```
- For commodities, futures prices give risk-neutral expectations directly.

## Types of real options
| Option | Like a… |
|---|---|
| Expand | call |
| Contract / abandon | put |
| Delay / timing | American call |
| Extend life | call |
| Switch inputs/outputs | portfolio of options |

## Valuing
- Build a tree for the underlying variable (often a trinomial tree for mean-reverting commodity prices).
- At each node, compare continuing vs exercising the flexibility.
- Value of option = project value with flexibility − without.

## Examples
Valuing a company (e.g., Amazon) as base business + growth options; valuing a resource project (oil field) with options to abandon/expand.

## Remember
- Uncertainty *increases* the value of flexibility — just like volatility increases option value.
