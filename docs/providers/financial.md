# Financial data

There is **no** single Government Loan API.

```
data.gov.in
official Ministry / Department portals
official State Government sources
JanSamarth / official credit-linked information (adapter boundary; no assumed generic public API)
↓
ingestion → normalize → validate
↓
PostgreSQL
↓
GovernmentSchemeRepository
↓
GovernmentSchemeProvider
↓
Financial Agent
```

AND

```
FinancialCalculator (Python)
↓
EMI, total_interest, total_repayment, schedule
```

Python owns numerical correctness. Official records own eligibility/limits/subsidy. OpenRouter only interprets. JanSamarth is not assumed to expose a generic public API.
