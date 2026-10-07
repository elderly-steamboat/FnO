# Ch 7 — Swaps

**TL;DR:** A swap exchanges one stream of cash flows for another. Value it either as **two bonds** or as a **portfolio of forwards/FRAs**.

## Plain-vanilla interest rate swap
- Pay fixed, receive floating (LIBOR) on a notional principal (never exchanged).
- Uses: turn a floating liability into fixed (or vice versa); turn an asset's return from fixed to floating.
- **Swap rate** = fixed rate that makes the swap worth zero today. Swap rates are close to AA-quality par yields.
- Comparative advantage argument (why swaps exist) is shaky — differences often reflect default-risk features of floating loans.

## Valuation
```
As bonds (receive fixed):  V_swap = B_fix − B_fl
  B_fl = (L + k*) e^(−r1 t1)   (floating bond is worth par right after a reset)
As FRAs: value each exchange assuming forward rates are realised, discount, sum.
```

## Currency swap
- Exchange principal *and* interest in two currencies.
- Value: `V = B_D − S0 · B_F` (receive domestic) or as a series of FX forwards.

## Credit risk
- Swap value can be + or −; credit exposure only when it's positive to you **and** the counterparty defaults.
- Currency swaps carry more credit risk than IRS (principal exchange at end).

## Other swaps
Basis, amortising, step-up, forward/deferred, constant maturity (CMS), compounding, equity swaps, swaptions, commodity, volatility, variance swaps.

## Remember
- Floating side = par at reset dates. That's why bond valuation is quick.
- For collateralised swaps the market now discounts at OIS rather than LIBOR.
