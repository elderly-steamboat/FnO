# Ch 19 — Volatility Smiles

**TL;DR:** If BSM were right, implied vol would be the same for all strikes. It isn't. The shape (smile/skew) tells you the market thinks the true distribution has fatter tails than lognormal.

## Key facts
- Put–call parity holds regardless of model ⇒ **calls and puts with same K, T have the same implied vol**.
- **Currency options: smile** (U-shape) → both tails fatter than lognormal. Cause: jumps, non-constant volatility.
- **Equity options: skew/smirk** (vol falls as K rises) → heavy left tail, thin right tail. Causes: leverage (price ↓ → debt/equity ↑ → vol ↑), **crashophobia** since 1987.
- **Volatility surface:** implied vol by strike and maturity; used to price non-standard options by interpolation.
- Smile usually less pronounced for long maturities.
- Smile measured against **moneyness** (K/S0 or K/F0, or delta).

## Greek letters with smiles
If vol depends on K/S, delta changes: `Δ = Δ_BSM + ν_BSM · ∂σ_imp/∂S`.

## Single large jump expected
Bimodal distribution (e.g., takeover news) → frown (inverted smile).

## Remember
- Using BSM with the "right" implied vol for each strike is how traders patch the model.
- The smile is the market's correction to BSM assumptions; models in Ch 26 try to explain it.
