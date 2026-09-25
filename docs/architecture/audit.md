# Architecture audit

Performed against the scaffold. Product features were not added.

## Checks

1. Next.js → FastAPI → Pydantic → FeasibilityService → LangGraph-shaped workflow → agents: **yes**
2. Six agents exist (plus final report): **yes**
3. First four independent (copies + merge): **yes**
4. Opportunity waits for four; SWOT waits for five: **yes** (`workflows/barriers.py`)
5. Real provider names (data.gov.in/AGMARKNET, Google Geocoding/Places/Routes, official gov ingest, OpenRouter URL): **yes**
6. No fictional Government Loan API: **yes**
7. Keys not `NEXT_PUBLIC_*` except API origin: **yes**
8. Calculator independent of LLM: **yes**
9. SourceMetadata on external objects: **yes**
10. Agents take interfaces in constructors: **yes**
11. Agents do not import httpx/sqlalchemy/google: **tested**
12. Opportunity/SWOT do not call market/geo/competition/gov providers: **tested via call counts**
13. Structured schemas for analyses: **yes**
14. Docs match this layout: **yes**

## Problems found / fixed during scaffold

None remaining in this empty-repo rewrite. Production HTTP and ingestion remain unimplemented by design.

## Remaining production work

See [remaining.md](./remaining.md).
