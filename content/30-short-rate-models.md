# Ch 30 — Interest Rate Derivatives: Models of the Short Rate

**TL;DR:** Model the instantaneous short rate r. Whole term structure follows from it. **Equilibrium models** (Vasicek, CIR) generate a curve; **no-arbitrage models** (Ho–Lee, Hull–White) are fitted to today's curve. Price with trees.

## Basics
- Zero-coupon bond: `P(t,T) = Ê[ e^(−∫r dτ) ]`.
- Rates show **mean reversion** — high rates tend to fall, low rates tend to rise.

## Equilibrium (one-factor)
| Model | Process | Notes |
|---|---|---|
| Rendleman–Bartter | `dr = μ r dt + σ r dz` | no mean reversion |
| **Vasicek** | `dr = a(b − r)dt + σ dz` | analytic bonds; r can go negative |
| **CIR** | `dr = a(b − r)dt + σ √r dz` | r stays ≥ 0 |
Bond price form: `P(t,T) = A(t,T) e^(−B(t,T) r)`; Vasicek `B = (1 − e^(−a(T−t)))/a`.
Problem: don't match today's term structure exactly.

## No-arbitrage
| Model | Process | Notes |
|---|---|---|
| **Ho–Lee** | `dr = θ(t)dt + σ dz` | θ(t) fitted to curve; no mean reversion |
| **Hull–White (extended Vasicek)** | `dr = [θ(t) − a r]dt + σ dz` | analytic bond & bond option prices |
| Black–Derman–Toy | lognormal r, built as a binomial tree | mean reversion tied to how σ(t) changes |
| **Black–Karasinski** | `d ln r = [θ(t) − a(t) ln r]dt + σ(t) dz` | r > 0, no analytics |

## Options on coupon bonds
Jamshidian's trick: decompose into options on zero-coupon bonds.

## Trees
- **Trinomial tree** (Hull–White): build for x with mean reversion (branching changes at edges), then shift each level to fit the zero curve.
- Handles American/Bermudan features (callable bonds, Bermudan swaptions).

## Calibration
Choose a and σ to fit market cap/swaption prices (minimise pricing errors). Hedge with zero-curve shifts and vega buckets.

## Remember
- One-factor models imply all rates move together — fine for many products, not for spread options (need multi-factor).
