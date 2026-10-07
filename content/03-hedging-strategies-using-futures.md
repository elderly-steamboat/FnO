# Ch 3 — Hedging Strategies Using Futures

**TL;DR:** Use futures to lock in a price. Hedges are rarely perfect because of **basis risk**; choose the number of contracts with the **optimal hedge ratio**.

## Core ideas
- **Short hedge:** you'll *sell* an asset later (own it) → short futures.
- **Long hedge:** you'll *buy* an asset later → long futures.
- **Arguments against hedging:** shareholders can diversify themselves; competitors may not hedge; a hedge that loses money looks bad even if it reduced risk.
- **Basis = spot − futures.** It's zero at delivery but uncertain before → *basis risk*. Choose a contract that expires *just after* the hedge ends, on the most correlated asset.
- **Cross hedging:** hedge asset ≠ futures asset (e.g., jet fuel hedged with heating oil).

## Key formulas
```
Effective price with hedge = F1 + b2          (F1 = initial futures, b2 = final basis)

Minimum-variance hedge ratio:  h* = ρ · σ_S / σ_F
Hedge effectiveness = ρ²       (regression of ΔS on ΔF)
Number of contracts:  N* = h* · Q_A / Q_F     (Q_A = exposure size, Q_F = contract size)
With daily settlement ("tailing"):  N* = h* · V_A / V_F   (values, not quantities)

Stock index hedge:  N* = β · V_portfolio / V_futures
Change beta from β to β*:  N = (β* − β) · V_A / V_F   (negative ⇒ short)
```

## Other bits
- Index futures let you change market exposure, or "pick stocks" while removing market risk.
- **Stack and roll:** roll short-dated futures forward to hedge long horizons — exposes you to rollover basis and cash-flow risk.

## Remember
- h* comes from a regression of spot changes on futures changes (slope = h*).
- A hedge reduces *variance*, not always losses.
