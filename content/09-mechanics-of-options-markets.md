# Ch 9 — Mechanics of Options Markets

**TL;DR:** How exchange-traded options work: contract specs, terminology, margins, clearing, and the four basic positions.

## Four positions
```
Long call:  max(S_T − K, 0)      Short call: −max(S_T − K, 0)
Long put:   max(K − S_T, 0)      Short put:  −max(K − S_T, 0)
```

## Terminology
- **In / at / out of the money:** for a call, S > K / S = K / S < K (reversed for puts).
- **Intrinsic value** = payoff if exercised now; **time value** = price − intrinsic.
- Option **class** (all calls or puts on a stock), **series** (same class, strike, expiry).
- Exchange options: 1 contract = 100 shares; expiry around 3rd Friday; strikes spaced by $2.50/$5/$10.
- **Weeklies, LEAPS** (long-dated), **FLEX** options (custom terms on exchange).

## Adjustments
- Stock splits n-for-m → strike × m/n, contracts × n/m. Stock dividends handled the same way. Cash dividends: no adjustment.
- Position and exercise limits apply.

## Trading & margins
- Market makers quote bid/ask; offsetting orders close positions.
- **Buyers pay in full** (no leverage via margin for short-dated options).
- **Writers post margin** (naked options need more than covered).
- **Options Clearing Corporation (OCC)** guarantees performance.

## Other option-like products
Warrants (issued by company → new shares), employee stock options, convertible bonds. These dilute; exchange options don't.

## OTC options
Tailored by banks; popular for FX and rates.

## Remember
- Exercising an American call early before expiry throws away time value (for non-dividend stocks — Ch 10).
