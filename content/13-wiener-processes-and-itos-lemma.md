# Ch 13 — Wiener Processes and Itô's Lemma

**TL;DR:** Stock prices are modelled as random walks in continuous time. Itô's lemma is the chain rule for such processes, letting us find how a function of the stock (like an option) moves.

## Building blocks
- **Markov property:** only today's price matters for the future (consistent with weak-form efficiency).
- **Wiener process z:** `Δz = ε√Δt`, ε ~ N(0,1); increments independent. Variance grows linearly with time.
- **Generalised Wiener:** `dx = a dt + b dz` (constant drift a, variance rate b²).
- **Itô process:** a and b can depend on x and t.

## Stock model — Geometric Brownian Motion (GBM)
```
dS = μ S dt + σ S dz
ΔS/S ~ N(μΔt, σ²Δt)
```
μ = expected return, σ = volatility. Percentage changes are normal over short intervals.

## Itô's lemma
If `dx = a dt + b dz` and G = G(x, t), then
```
dG = (∂G/∂x · a + ∂G/∂t + ½ ∂²G/∂x² · b²) dt + ∂G/∂x · b dz
```
The extra ½ b² G_xx term is what differs from ordinary calculus.

## Key applications
```
Forward on non-dividend stock F = S e^(r(T−t)):  dF = (μ − r) F dt + σ F dz
G = ln S:  dG = (μ − σ²/2) dt + σ dz   ⇒ ln S_T ~ N(ln S0 + (μ − σ²/2)T, σ²T)
```
So S_T is **lognormal**.

## Remember
- Correlated processes: `dz1 dz2 = ρ dt`.
- The σ²/2 adjustment between arithmetic mean return (μ) and geometric/compound return (μ − σ²/2) shows up everywhere.
