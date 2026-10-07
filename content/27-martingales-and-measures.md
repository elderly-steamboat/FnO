# Ch 27 — Martingales and Measures

**TL;DR:** Generalises risk-neutral valuation. Pick any tradeable asset as **numeraire**; in the matching measure, every price divided by that numeraire is a **martingale**. Choosing a clever numeraire makes pricing easy — the backbone of interest rate models.

## Key ideas
- **Market price of risk λ:** `(μ − r)/σ` — same for all derivatives depending on the same variable.
```
μ − r = λ σ
```
- **Multiple sources of risk:** `μ − r = Σ λ_i σ_i`.
- **Martingale:** expected future value = today's value (zero drift).
- **Equivalent martingale measure:** if f, g are traded, f/g is a martingale in the world where market price of risk = σ_g.

## Numeraire choices
| Numeraire g | Measure | Pricing formula |
|---|---|---|
| Money market account | traditional risk-neutral | `f0 = E[ e^(−∫r dt) f_T ]` |
| Zero-coupon bond P(0,T) | T-forward risk-neutral | `f0 = P(0,T) E_T[f_T]`; forward price = expected future price |
| Annuity A(t) | swap measure | swap rate is a martingale (swaptions) |

- In the T-forward measure, the forward rate for period ending T is a martingale → justifies Black's model for rates.

## Extensions
- **Multiple variables:** each variable's drift changes by its correlation with the numeraire's volatility.
- **Exchange option (Margrabe)** falls out by choosing one asset as numeraire.
- **Change of numeraire rule:** switching from g to h adds `ρ σ_v (σ_h − σ_g)` to the drift of variable v.

## Remember
- "Expected value under the right measure, times the numeraire" — that's all pricing is.
