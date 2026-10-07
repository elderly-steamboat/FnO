# Ch 10 — Properties of Stock Options

**TL;DR:** Without any model, pure no-arbitrage gives bounds on option prices, put–call parity, and rules for early exercise.

## What moves option prices
| Factor ↑ | Euro call | Euro put | Amer call | Amer put |
|---|---|---|---|---|
| Stock price S0 | + | − | + | − |
| Strike K | − | + | − | + |
| Time to expiry T | ? | ? | + | + |
| Volatility σ | + | + | + | + |
| Risk-free rate r | + | − | + | − |
| Dividends | − | + | − | + |

## Bounds (no dividends)
```
Call:  max(S0 − K e^(−rT), 0) ≤ c ≤ S0
Put:   max(K e^(−rT) − S0, 0) ≤ p ≤ K e^(−rT)
```

## Put–call parity (European, no dividends)
```
c + K e^(−rT) = p + S0
```
Both sides pay max(S_T, K) at expiry. With dividends: replace S0 by S0 − D.

American bounds: `S0 − K ≤ C − P ≤ S0 − K e^(−rT)`.

## Early exercise
- **American call on non-dividend stock: never exercise early** → C = c. Reasons: lose insurance, lose interest on K. Better to sell it.
- **American put:** early exercise *can* be optimal when deep in the money (getting K now earns interest).
- With dividends: call early exercise might be optimal just before ex-dividend date.

## Remember
- Parity is the most-used identity in the book: it converts calls ⇄ puts and checks quotes for arbitrage.
