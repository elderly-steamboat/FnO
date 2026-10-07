# Ch 6 — Interest Rate Futures

**TL;DR:** Treasury bond futures and Eurodollar futures let you hedge rate moves. Duration-based hedging sizes the position.

## Day counts & quotes
- Day counts: Treasury bonds **actual/actual**, corporate bonds **30/360**, money market **actual/360**.
- **Clean price** (quoted) vs **dirty/cash price** = clean + accrued interest.
- T-bill quoted as a **discount rate**: `P = 360/n · (100 − Y)` (Y = cash price per 100).

## Treasury bond futures
- Short can deliver any bond in a range; price adjusted by a **conversion factor** (bond's price at a 6% yield).
- Cash received by short = `settlement price × CF + accrued interest`.
- **Cheapest-to-deliver (CTD):** the bond minimising `quoted price − settlement price × CF`. When yields > 6% long, high-coupon short bonds tend not to be CTD; long-duration low-coupon bonds tend to be.
- Short also has timing options (wild card play) → futures slightly lower than a simple model.

## Eurodollar futures
- On 3-month rate; quote `Q = 100 − R`. 1 bp move = **$25** per contract.
- Settled to the 3-month rate at maturity — used to build long-end of the LIBOR curve.
- **Convexity adjustment:** futures rate > forward rate. Ho–Lee approx:
```
Forward rate = Futures rate − ½ σ² T1 T2
```

## Duration-based hedging
```
N* = (P · D_P) / (V_F · D_F)
```
P = portfolio value, D_P its duration, V_F futures contract price, D_F duration of the underlying (CTD) at hedge maturity.

## Remember
- Duration hedging only protects against parallel shifts.
- Asset-liability management in banks matches durations to limit this risk.
