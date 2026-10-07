# Ch 28 — Interest Rate Derivatives: The Standard Market Models

**TL;DR:** The market prices bond options, caps/floors, and swaptions with versions of **Black's model**, each justified by choosing the right numeraire (Ch 27).

## Bond options
- Embedded in callable/putable bonds. Black's model on the **forward bond price** F_B:
```
c = P(0,T) [F_B N(d1) − K N(d2)],   d1 = [ln(F_B/K) + σ_B² T/2] / (σ_B √T)
```
- Use cash (dirty) prices. Yield-volatility conversion: `σ_B ≈ D · y0 · σ_y` (D = modified duration of forward bond).

## Caps & floors
- **Cap** = series of **caplets**; each caplet pays `L δ max(R_k − R_K, 0)` at t_{k+1}.
- A caplet = put on a zero-coupon bond.
- Black's model per caplet (F_k = forward rate, σ_k its vol):
```
caplet = L δ_k P(0, t_{k+1}) [F_k N(d1) − R_K N(d2)]
d1 = [ln(F_k/R_K) + σ_k² t_k/2] / (σ_k √t_k)
```
- **Floor** = series of floorlets; **collar** = long cap + short floor.
- Parity: `cap − floor = swap`.
- **Flat vols** (one per cap) vs **spot vols** (one per caplet). Vol "hump" ~ 2–3 years.

## European swaptions
- Option to enter a swap at rate R_K. Payer swaption = call on the swap rate.
```
Payer = L A [s_F N(d1) − R_K N(d2)],  A = Σ δ_i P(0, T_i)   (annuity)
```
- Payer swaption = put on a coupon bond; receiver = call.
- Market quotes swaption vols by expiry × swap tenor.

## Hedging
Greeks with respect to the zero curve: **DV01**, bucket deltas, partial durations; gamma and vega similarly.

## Remember
- Black's model isn't one model: forward bond prices, forward rates and swap rates *can't all* be lognormal at once — each is consistent under its own measure.
