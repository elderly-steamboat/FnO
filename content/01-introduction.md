# Ch 1 — Introduction

**TL;DR:** A derivative is a contract whose value depends on something else (a stock, rate, commodity…). Three kinds of people use them: hedgers, speculators, arbitrageurs.

## Core ideas
- **Where they trade:** exchanges (standardised, clearing house removes counterparty risk) vs **OTC** (custom, bilateral, now mostly centrally cleared after 2008). OTC is far bigger by notional.
- **Forward:** agree today to buy/sell at a fixed price on a future date. Long = buyer, short = seller. Costs nothing to enter.
- **Futures:** a forward traded on an exchange, standardised and settled daily.
- **Option:** the *right, not obligation*. **Call** = right to buy, **put** = right to sell, at the **strike** K by the **expiry** T. You pay a premium for it.
  - American = exercise any time; European = only at expiry.

## Payoffs (at expiry, S_T = asset price)
```
Long forward:  S_T − K          Short forward: K − S_T
Long call:     max(S_T − K, 0)  Long put:      max(K − S_T, 0)
```

## Who uses them
| Type | Goal | Example |
|---|---|---|
| Hedger | reduce risk | exporter locks in an FX rate with a forward |
| Speculator | bet on direction, with leverage | buy calls instead of shares |
| Arbitrageur | riskless profit from mispricing | same stock cheaper in London than New York |

## Remember
- Forwards **lock in** a price (remove upside and downside); options **insure** (keep upside, cost a premium).
- Leverage cuts both ways — big derivative losses (Barings, SocGen) came from people exceeding risk limits.
