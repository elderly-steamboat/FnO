# Ch 4 — Interest Rates

**TL;DR:** The language of rates: compounding conventions, zero rates, bond pricing, forward rates, FRAs, duration and convexity. Everything later builds on this.

## Types of rates
- **Treasury rates** (government), **LIBOR** (bank borrowing, now replaced by RFRs like SOFR), **repo** (secured), **OIS / fed funds** (overnight). Derivative traders treat LIBOR/OIS as the "risk-free" benchmark rather than Treasuries.

## Compounding
```
m times a year:   A = P(1 + R/m)^(m·n)
Continuous:       A = P e^(R·n)
Convert:          Rc = m ln(1 + Rm/m)     Rm = m(e^(Rc/m) − 1)
```
Use continuous compounding in this book unless stated.

## Zero rates & bonds
- **Zero rate** = yield on a single cash flow at time T.
- **Bond price** = sum of cash flows each discounted at its own zero rate.
- **Yield** = single rate that discounts all flows to the price. **Par yield** = coupon making price = face value.
- **Bootstrap:** build the zero curve from bond prices, short maturities first.

## Forward rates
```
R_F = (R2·T2 − R1·T1) / (T2 − T1) = R2 + (R2 − R1)·T1/(T2 − T1)
```
Upward-sloping zero curve ⇒ forward > zero rate.

## FRA (forward rate agreement)
Locks in rate R_K on principal L for period T1–T2. Value = PV of `L·(R_K − R_F)·(T2 − T1)` (receiver of fixed). Valued by assuming forward rates are realised.

## Duration & convexity
```
Duration D = Σ t_i · (c_i e^(−y t_i)) / B       ΔB ≈ −B·D·Δy
Modified duration (annual comp.): D* = D/(1 + y/m)
Convexity C = Σ c_i t_i² e^(−y t_i) / B        ΔB/B ≈ −D·Δy + ½C(Δy)²
```
Duration ≈ weighted-average time of cash flows; only handles **parallel** small shifts.

## Term-structure theories
Expectations, market segmentation, **liquidity preference** (most realistic: investors prefer short, so long rates carry a premium → curves usually slope up).

## Remember
- Banks manage the gap between assets and liabilities by duration matching; most yield-curve risk isn't parallel though.
