# Ch 33 — Energy and Commodity Derivatives

**TL;DR:** Commodities behave differently from financial assets: they mean-revert, are seasonal, can't always be stored, and have spikes. Models add these features; weather and insurance derivatives are covered too.

## Markets
- **Agricultural** (corn, wheat, livestock), **metals** (gold, copper), **energy** (crude oil, natural gas, electricity).
- Electricity can't be stored → very high volatility and **price spikes**; contracts specify delivery periods.
- Natural gas: seasonal, storage-limited.

## Modelling
- **Mean reversion** toward a level that can vary with time/season:
```
d ln S = [θ(t) − a ln S] dt + σ dz
```
- Calibrate to the futures curve (which encodes expected spot under risk-neutral measure).
- Add **jumps** for spikes (electricity, gas).
- Trees like Hull–White are adapted for these.

## Weather derivatives
- Based on **HDD** (heating degree days) = max(65°F − avg temp, 0), **CDD** (cooling degree days) = max(avg temp − 65°F, 0).
- Used by energy firms to hedge demand volume risk.
- Weather risk is mostly **unsystematic** → price using real-world expectations, discounted at risk-free.

## Insurance derivatives
- **Catastrophe (CAT) bonds:** high coupon, principal lost if insured losses exceed a level.
- Low correlation with markets → expected loss priced at real-world probabilities.

## Energy producer risk
Hedge both **price** and **volume** (quantity) risk — weather derivatives help with volume.

## Remember
- Futures curves (contango/backwardation) carry information about storage and convenience yield.
