# Ch 12 — Binomial Trees

**TL;DR:** Model the stock moving up or down each step. Build a riskless portfolio → option price doesn't depend on real-world probabilities. Price by **risk-neutral valuation**: expected payoff under probability p, discounted at r.

## One step
- Stock: S0 → S0·u or S0·d. Option payoffs fu, fd.
- Hold Δ shares and short 1 option: riskless if
```
Δ = (fu − fd) / (S0 u − S0 d)
```
- Price:
```
f = e^(−rΔt) [p·fu + (1 − p)·fd]
p = (e^(rΔt) − d) / (u − d)
```

## Risk-neutral valuation
In a risk-neutral world all assets earn r. Prices computed there are correct in the real world too — the real expected return μ never appears.

## Multi-step & American options
- Work backward from expiry.
- **American:** at each node take `max(continuation value, early exercise payoff)`.
- Delta changes node to node → hedge must be rebalanced.

## Matching volatility (Cox–Ross–Rubinstein)
```
u = e^(σ√Δt),   d = 1/u
```

## Other underlyings (replace e^(rΔt) by a):
```
No dividends:        a = e^(rΔt)
Index (yield q):     a = e^((r − q)Δt)
Currency:            a = e^((r − rf)Δt)
Futures:             a = 1
p = (a − d)/(u − d)
```

## Remember
- As steps → ∞ the tree converges to Black–Scholes–Merton (Ch 14).
- Real-world p would require a different (unknown) discount rate — risk-neutral avoids that problem.
