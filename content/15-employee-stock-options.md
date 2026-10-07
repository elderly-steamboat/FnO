# Ch 15 — Employee Stock Options

**TL;DR:** Companies grant at-the-money call options to employees. They're long-dated, non-transferable, and usually exercised early, so standard BSM must be adjusted. Must be expensed at fair value.

## Contract features
- Typical life 10 years, **vesting period** (e.g. 1–4 years) — leave before vesting = lose options.
- Can't be sold → employees exercise early (and immediately sell shares) to cash out or diversify.
- Exercise creates new shares → **dilution**.
- Usually **at-the-money** when granted.

## Do they align incentives?
Pros: tie pay to shareholder value. Cons: reward volatility/short-termism; temptation to time announcements or massage results around grant/vesting dates.

## Accounting
- Since 2005 (FAS 123R / IFRS 2): expensed at **fair value on grant date**.

## Valuation approaches
1. **BSM with expected life** instead of contractual life (quick, crude).
2. **Binomial tree** with rules: exercise when price hits a multiple of K; exit rates for employees leaving.
3. **Market-based** (e.g., Microsoft-style auctions or tradeable instruments).
- Dilution adjustment like warrants.

## Backdating scandal
Some firms secretly set grant dates to past low prices (instantly in the money). Discovered via statistical patterns of abnormal returns; SEC now requires prompt reporting (2 business days).

## Remember
- Early exercise + non-transferability → ESO worth *less* than an equivalent tradeable option.
