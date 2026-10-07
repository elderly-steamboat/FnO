# Ch 29 — Convexity, Timing, and Quanto Adjustments

**TL;DR:** Black's model assumes the "expected value = forward" rule. Some products break the rule because of *when* or *in what currency* they pay, or because the payoff is non-linear in a rate. Fix with small adjustments to the forward.

## Convexity adjustment
- Bond prices are convex in yields → **expected forward yield ≠ forward yield**.
- Applies when a payoff depends on a bond **yield** (e.g., CMS rates) paid at a time not matching the natural measure.
```
E_T(y_T) ≈ y0 − ½ y0² σ_y² T · G''(y0)/G'(y0)
```
(G = forward bond price as a function of yield.) Adjustment is usually *upward*.

## Timing adjustment
- Rate observed at T but paid at T* ≠ natural time.
- Expected value of variable V moves from its T-forward value by roughly
```
E_{T*}(V_T) ≈ E_T(V_T) · exp[ − ρ σ_V σ_R · R0 (T* − T) · T / (1 + R0 (T* − T)) ]
```
  (R = rate between T and T*, ρ = correlation of V with R.) Small but not zero.
- Example: LIBOR-in-arrears swaps (rate set and paid at the same date) need a timing/convexity adjustment.

## Quanto adjustment
- Payoff in currency Y on variable measured in currency X (e.g., Nikkei futures paid in USD).
- Drift change ≈ `ρ σ_V σ_S` (correlation of the variable with the FX rate × their vols).
- Also needed for **differential swaps (diff swaps)**.

## Siegel's paradox
Expected exchange rate in one currency ≠ inverse of expected rate in the other — a measure effect, resolved by the same tools.

## Remember
- These are all "the expected value under the *wrong* measure" fixes. Small for short maturities, important for long ones.
