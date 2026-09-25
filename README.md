# GraminAI

Multilingual AI business feasibility platform for rural and semi-urban entrepreneurs.

**This repository is architecture and scaffolding.** Real Google Maps, data.gov.in, and OpenRouter HTTP calls, production prompts, and a polished UI are **not** implemented.

## Architecture

```
USER → Next.js → HTTPS REST → FastAPI → Pydantic → Feasibility Service
  → LangGraph orchestrator
  → Market | Geographic | Competition | Financial   (parallel)
  → wait for 4 → Opportunity → wait for 5 → SWOT → Final report
  → FastAPI → Next.js → USER
```

OpenRouter is an LLM **gateway**, not an agent. EMI and repayment figures come from a Python calculator. Scheme facts come from official sources after ingestion into PostgreSQL.

## Monorepo

| Path | Purpose |
| --- | --- |
| `apps/web` | Next.js presentation; talks only to FastAPI |
| `apps/api` | FastAPI, agents, providers, workflow, calculator |
| `packages/types` | Shared TypeScript request/response types |
| `packages/contracts` | JSON Schema copies of domain contracts |
| `packages/config` | Shared TS config |
| `docs/` | Architecture, providers, API, decisions |
| `scripts/` | Local helpers |

## Environment

Copy `.env.example`. Keys stay on the API process:

- `OPENROUTER_API_KEY`, `OPENROUTER_MODEL`
- `GOOGLE_MAPS_API_KEY`
- `DATA_GOV_IN_API_KEY`
- `DATABASE_URL`
- provider selection flags (`MARKET_DATA_PROVIDER`, …)

`NEXT_PUBLIC_API_URL` is the FastAPI origin only.

## Run API

```bash
cd apps/api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Health: `GET http://localhost:8000/health` → `{"status":"ok"}`

## Run web

```bash
npm install
npm run web
```

## Tests

```bash
cd apps/api && pytest
python scripts/check_imports.py
```

## Real providers (planned adapters)

| Agent | Provider / API | Role |
| --- | --- | --- |
| Market | data.gov.in / AGMARKNET | Mandi/commodity **prices** |
| Geographic | Google Geocoding, Places (New), Routes | Coordinates, nearby places, distance |
| Competition | Google Places API (New) | Place/business discovery |
| Financial | Official gov sources → PostgreSQL + Python calculator | Schemes + EMI |
| LLM agents | OpenRouter `POST /api/v1/chat/completions` | Structured analysis |
