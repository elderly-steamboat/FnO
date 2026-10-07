# Ch 26 — More on Models and Numerical Procedures

**TL;DR:** Models that fix BSM's flaws (smiles, jumps, stochastic vol) and special numerical tricks for awkward products (path-dependence, barriers, convertibles).

## Alternatives to BSM
| Model | Idea | Smile it produces |
|---|---|---|
| **CEV** | `dS = (r − q)S dt + σ S^α dz` | α < 1: equity-like skew |
| **Merton jump-diffusion** | GBM + Poisson jumps (lognormal size) | fat tails, strong short-dated smile |
| **Variance-gamma** | Brownian motion run on random "business time" | skew/kurtosis via ν, θ |
| **Stochastic volatility** (Hull–White, Heston) | σ itself random, mean-reverting | smile flattening with maturity; negative corr → skew |
| **Implied volatility function (IVF / local vol)** | σ(S, t) fitted to match all vanilla prices exactly | matches today's surface; dynamics can be wrong |

## Numerical techniques for tricky products
- **Convertible bonds:** tree on stock with default intensity; at each node, value = max(hold, convert), subject to call by issuer.
- **Path-dependent derivatives:** add a state variable (e.g., running average/maximum) at each node (Hull–White approach).
- **Barrier options:** place tree nodes exactly on the barrier; adaptive mesh; trinomial adjustments.
- **Two correlated assets:** transform to uncorrelated variables, 3-D trees, or adjust probabilities.
- **Monte Carlo for American options:** Longstaff–Schwartz (least-squares regression) or parameterised exercise boundary.

## Remember
- Matching today's vanilla prices (IVF) isn't enough: exotics depend on how the smile *moves* — model choice matters.
