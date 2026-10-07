# Ch 31 — Interest Rate Derivatives: HJM and LMM

**TL;DR:** Instead of modelling just the short rate, model the **whole forward curve**. HJM is the general framework (continuous forwards); LMM (LIBOR Market Model) models the market-observable forward LIBOR rates and is consistent with Black's caplet pricing.

## Heath–Jarrow–Morton (HJM)
- Model instantaneous forward rates f(t,T) directly.
- **Key result:** under risk-neutral measure, the drift is fixed by the volatilities:
```
df(t,T) = m(t,T)dt + s(t,T)dz,   m(t,T) = s(t,T) ∫_t^T s(t,τ)dτ
```
- Can be multi-factor. Downside: usually **non-Markov** → bushy trees; Monte Carlo needed.

## LIBOR Market Model (LMM / BGM)
- Model discrete forward rates F_k for periods [t_k, t_{k+1}].
- Under the matching forward measure each F_k is lognormal → Black caplet prices are exact.
- Under a common (rolling forward) measure:
```
dF_k / F_k = Σ_{i=m(t)}^{k} [δ_i F_i σ_i σ_k ρ_{ik} / (1 + δ_i F_i)] dt + σ_k dz_k
```
- Volatility calibrated directly from **caplet vols**; correlation from history or swaption prices.
- Multi-factor: allows rates to move differently (twists).
- Swaption pricing: approximate swap-rate vol from forward rate vols (Rebonato formula).
- **Bermudan swaptions:** Monte Carlo + Longstaff–Schwartz or exercise boundary.
- Extensions: CEV/stochastic-vol LMM to fit smiles.

## Agency mortgage-backed securities
- Pools of mortgages; borrowers' **prepayment option** makes cash flows depend on rates.
- **CMOs** (tranches by prepayment priority), **IOs/POs** (interest-only / principal-only strips — IO value rises when rates rise).
- Valued with Monte Carlo + a prepayment model; quoted via **option-adjusted spread (OAS)**.

## Remember
- HJM/LMM drift is not free: no-arbitrage ties it to the volatilities.
