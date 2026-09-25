# API

## GET /health

```json
{ "status": "ok" }
```

## POST /api/v1/feasibility

Validated by `FeasibilityRequest`. Route calls `FeasibilityService` only.

Example body:

```json
{
  "business": "dairy farm",
  "location": "Mysuru",
  "budget": 500000,
  "own_investment": 150000,
  "loan_required": 350000,
  "language": "kn"
}
```

Response is `FinalReport` JSON.

This architecture phase wires **mock providers** into the default service so the route can be exercised without API keys. Empty observed datasets are not live mandi/Places data.
