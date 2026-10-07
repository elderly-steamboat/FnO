# Ch 20 — Basic Numerical Procedures

**TL;DR:** When no formula exists (American options, exotic payoffs), use **trees**, **Monte Carlo**, or **finite differences**.

## Binomial trees (in practice)
```
u = e^(σ√Δt),  d = 1/u,  p = (a − d)/(u − d),  a = e^((r − q)Δt)
```
- Delta, gamma, theta read off the tree; vega and rho by bumping inputs.
- **Control variate:** price American and European on the same tree; adjust American by `BSM_European − tree_European` (improves accuracy).
- **Known dividends:** tree on S minus PV(dividends) to keep it recombining.
- **Alternatives:** trinomial trees, time-dependent parameters, **adaptive mesh** near the strike.

## Monte Carlo
- Simulate paths in a risk-neutral world: `S(t+Δt) = S(t) exp[(r − q − σ²/2)Δt + σ ε √Δt]`.
- Price = discounted average payoff. Standard error = ω/√M (M samples) — accuracy grows slowly.
- Good for path-dependent payoffs and many underlyings (multi-dimensional). Correlated normals via **Cholesky**.
- **Variance reduction:** antithetic variates, control variates, importance sampling, stratified sampling, moment matching, **quasi-random** (low-discrepancy) sequences.
- **American options:** Longstaff–Schwartz (regress continuation value) or optimal exercise boundary parameterisation.

## Finite difference methods
Solve the BSM PDE on a grid of S and t, working back from expiry.
- **Implicit:** stable, solve linear system each step.
- **Explicit:** simpler, like a trinomial tree; can be unstable. Using ln S improves it.
- **Crank–Nicolson:** average of the two, faster convergence.

## Which to use
| | Trees | Monte Carlo | Finite diff. |
|---|---|---|---|
| American | ✅ | harder | ✅ |
| Path-dependent | limited | ✅ | limited |
| Many variables | ❌ | ✅ | ❌ |

## Remember
- MC error falls like 1/√M: 4× paths to halve error.
