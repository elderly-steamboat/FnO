# Ch 16 — Options on Stock Indices and Currencies

**TL;DR:** Treat the index or currency as a stock paying a continuous yield q (dividend yield for indices, foreign rate r_f for currencies). Swap S0 for S0 e^(−qT) in BSM.

## Key formulas (Merton's extension, yield q)
```
c = S0 e^(−qT) N(d1) − K e^(−rT) N(d2)
p = K e^(−rT) N(−d2) − S0 e^(−qT) N(−d1)
d1 = [ln(S0/K) + (r − q + σ²/2)T] / (σ√T),   d2 = d1 − σ√T
Parity: c + K e^(−rT) = p + S0 e^(−qT)
Currency: q = r_f.  Can also write with forward: F0 = S0 e^((r − q)T)
c = e^(−rT)[F0 N(d1) − K N(d2)]
```
Binomial: `a = e^((r − q)Δt)`.

## Index options
- Usually cash-settled, often European (S&P 500 SPX); 1 contract = 100 × index.
- **Portfolio insurance:** buy puts on index; number = β × (portfolio value / index value). If β ≠ 1, use CAPM to pick the strike.

## Currency options
- OTC market much bigger than exchange. Used for hedging FX exposure.
- **Range forward:** buy put + sell call (zero cost) → exchange rate locked into a band.
- **Exotics:** knock-outs, averages are common.

## Remember
- Any underlying with a yield fits the same template — that's the main reuse idea of this chapter.
