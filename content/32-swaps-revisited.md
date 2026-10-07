# Ch 32 — Swaps Revisited

**TL;DR:** Beyond plain-vanilla: many swaps can be priced by "assume forward rates are realised" plus convexity/timing/quanto adjustments where needed; those with embedded options need models.

## Variations on vanilla
- Different payment frequencies/day counts, compounding swaps, amortising/step-up principal, **forward swaps**, LIBOR-plus-spread.
- **Rule:** if the floating payment is the "natural" one (rate for a period, paid at the period's end), value as if forwards are realised. Otherwise adjust.

## Swaps needing adjustments
- **LIBOR-in-arrears:** rate set at payment date → convexity adjustment.
- **CMS / CMT swaps:** pay a swap/Treasury rate → convexity (+ timing) adjustment.
- **Differential (diff) swaps:** foreign rate applied to domestic notional → quanto adjustment.

## Equity swaps
Total return on an index vs LIBOR on the same notional; worth zero at start and at each reset.

## Swaps with embedded options
- **Accrual swaps:** fixed side accrues only when rate stays in a range → series of binary options.
- **Cancelable swaps:** one side can terminate → swap + Bermudan swaption.
- **Cancelable compounding swaps.**

## Other swaps
Commodity swaps, volatility/variance swaps, **index amortising rate swaps** (principal falls as rates fall, like mortgage prepayments), "bizarre" deals like the **Procter & Gamble** 5/30 swap (lost ~$100m).

## Remember
- When something about the timing, currency, or rate type is "unnatural", expect an adjustment.
