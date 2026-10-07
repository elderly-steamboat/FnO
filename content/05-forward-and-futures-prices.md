# Ch 5 — Determination of Forward and Futures Prices

**TL;DR:** Forward price = spot grown at the **cost of carry**. If it differs, arbitrage (buy cheap, sell rich).

## Investment vs consumption assets
- **Investment assets** (stocks, bonds, gold): held to invest → arbitrage works both ways → exact formulas.
- **Consumption assets** (oil, copper): held to use → only an *upper bound*.
- **Short selling:** sell borrowed asset, pay any income to the lender.

## Key formulas (continuous compounding, T = maturity)
```
No income:               F0 = S0 e^(rT)
Known cash income (PV=I): F0 = (S0 − I) e^(rT)
Known yield q:           F0 = S0 e^((r − q)T)
Stock index (div yield q): F0 = S0 e^((r − q)T)
Currency (foreign rate rf): F0 = S0 e^((r − rf)T)     ← interest rate parity
Commodity w/ storage U (PV): F0 = (S0 + U) e^(rT)
Consumption commodity:   F0 ≤ S0 e^((r + u − y)T)   y = convenience yield
Cost of carry c:         F0 = S0 e^(cT) (investment);  S0 e^((c − y)T) (consumption)
```

## Value of an existing forward (long, delivery price K)
```
f = (F0 − K) e^(−rT)
```

## Arbitrage logic
- F0 too high → borrow, buy spot, short forward (**cash-and-carry**).
- F0 too low → short spot, invest, go long forward (**reverse cash-and-carry**).

## Futures vs forwards
Equal if rates are constant/known. If the asset is positively correlated with rates, futures are slightly higher (daily gains can be reinvested at higher rates).

## Futures and expected spot
- **Normal backwardation:** F < E(S_T) (asset has positive systematic risk).
- **Contango:** F > E(S_T).
(These terms are also used loosely for downward/upward-sloping futures curves.)

## Remember
- A forward contract is worth 0 at inception; F0 is the delivery price that makes it so.
