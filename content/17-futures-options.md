# Ch 17 — Futures Options

**TL;DR:** An option on a futures contract. Exercise gives you a futures position plus cash = F − K (call). Price it with **Black's model** — same as an asset with yield q = r.

## Mechanics
- Exercise a call → long futures + cash `F − K` (latest settlement price).
- Exercise a put → short futures + cash `K − F`.
- Popular because futures are more liquid and easier to deliver than the asset, and you don't need to know the spot price.
- Most are American.

## Key formulas
```
Put–call parity: c + K e^(−rT) = p + F0 e^(−rT)

Black's model (European):
c = e^(−rT) [F0 N(d1) − K N(d2)]
p = e^(−rT) [K N(−d2) − F0 N(−d1)]
d1 = [ln(F0/K) + σ²T/2] / (σ√T),   d2 = d1 − σ√T
```
- Futures drift is **zero** in a risk-neutral world → a = 1 in trees, p = (1 − d)/(u − d).

## Futures-style options
Pay premium via daily settlement (no upfront). If futures and option expire together, their value equals the option on the asset.

## Futures options vs spot options
Same if both expire together (European). American futures options may be exercised early more often.

## Remember
- Black's model is reused for bond options, caps, swaptions (Ch 28) — just change F0 and the discount factor.
