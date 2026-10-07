# Ch 11 — Trading Strategies Involving Options

**TL;DR:** Combine options (with each other or with the stock) to shape the payoff to your view: direction, range, or volatility.

## Option + stock
- **Covered call:** long stock + short call → caps upside, earns premium.
- **Protective put:** long stock + long put → insurance floor.
- Put–call parity explains why these look like a short put / long call respectively.
- **Principal-protected note:** zero-coupon bond + call → can't lose principal, keeps some upside.

## Spreads (same type, different strikes or dates)
| Strategy | Built from | View |
|---|---|---|
| Bull spread | long call K1, short call K2 (K1<K2) — or puts | moderate rise, capped gain/loss |
| Bear spread | long put K2, short put K1 — or calls | moderate fall |
| Box spread | bull call + bear put | riskless: pays K2−K1 (check for arbitrage) |
| Butterfly | long K1, long K3, short 2×K2 | price stays near K2 |
| Calendar | short near-dated, long far-dated, same K | price stays near K |
| Diagonal | different K and T | mix |

## Combinations (calls and puts together)
| Strategy | Built from | View |
|---|---|---|
| Straddle | long call + long put, same K | big move either way |
| Strip / Strap | 1C+2P / 2C+1P | big move, tilted down / up |
| Strangle | long put K1 + long call K2 | big move, cheaper than straddle |
| Short versions | reverse | quiet market (unlimited risk) |

## Remember
- Any payoff that's piecewise-linear can be built from calls/puts at different strikes (European).
- Long volatility = buy straddles/strangles; short volatility = sell them.
