# Ch 18 — The Greek Letters

**TL;DR:** Greeks measure how an option's value changes with each input. Traders hedge by keeping Greeks near zero: delta daily, gamma and vega with other options.

## The Greeks (European, yield q; for non-dividend set q = 0)
| Greek | Meaning | Call | Put |
|---|---|---|---|
| **Delta Δ** | ∂V/∂S | e^(−qT) N(d1) | e^(−qT)[N(d1) − 1] |
| **Gamma Γ** | ∂²V/∂S² | N'(d1) e^(−qT) / (S0 σ√T) | same |
| **Vega ν** | ∂V/∂σ | S0 √T N'(d1) e^(−qT) | same |
| **Theta Θ** | ∂V/∂t (time decay) | usually − | usually − |
| **Rho ρ** | ∂V/∂r | K T e^(−rT) N(d2) | −K T e^(−rT) N(−d2) |

Long options: + gamma, + vega, − theta.

## Hedging ideas
- **Naked / covered positions** risky; **stop-loss** strategy fails (transaction costs, gaps).
- **Delta hedging:** hold −Δ shares per option; rebalance → cost ≈ option price.
- **Gamma:** curvature; rebalance more often when Γ big. Neutralise with another option: `w_T = −Γ / Γ_T`.
- **Vega:** neutralise with options too; need two traded options to be both gamma- and vega-neutral.
- Futures-based delta: `H_F = e^(−(r−q)T) H_A`.

## Relationship from BSM PDE
```
Θ + r S Δ + ½ σ² S² Γ = r Π
```
For a delta-neutral portfolio: big +Γ ⇔ big −Θ.

## In practice
- Traders: delta-neutral daily; gamma/vega monitored, managed when they get large.
- **Scenario analysis:** tables of P&L over S and σ grids.
- **Portfolio insurance** by synthetic puts (dynamic hedging) contributed to the 1987 crash.

## Remember
- Delta of the underlying = 1, its gamma = 0 → you *can't* fix gamma with stock alone.
