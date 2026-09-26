# 🌾 GraminAI

### Multilingual AI-Powered Business Advisory Platform for Rural & Semi-Urban Entrepreneurs

GraminAI is a planned multilingual AI business advisory platform designed to help rural and semi-urban entrepreneurs evaluate business opportunities through structured **market, geographic, competition, financial, opportunity, and SWOT analysis**.

The system is designed around a LangChain / LangGraph workflow containing four independent first-level analysis agents:

* Market Agent
* Geographic Agent
* Competition Agent
* Financial Agent

These agents produce structured results independently. Once all four results are available, the workflow passes them to the Opportunity Agent. The SWOT Agent then consumes the four first-level analyses together with the Opportunity analysis before the final report is generated.

> **Current Status:** Architecture & Scaffolding Phase  
> This repository currently focuses on system architecture, project structure, workflow design, schemas, interfaces, and documentation. Production implementation of live Google Maps, data.gov.in, OpenRouter HTTP, government-scheme ingestion, chatbot intelligence, and polished frontend workflows will be developed in subsequent phases.

> **Repository note:** The runnable tree in this clone is `apps/web` (Next.js) and `apps/api` (FastAPI). The `frontend/` / `backend/` layout in the architecture diagrams below is the conceptual target described in the original write-up.

---

# 📌 Table of Contents

* [Overview](#-overview)
* [Problem Statement](#-problem-statement)
* [Goals](#-goals)
* [Planned Features](#-planned-features)
* [System Architecture](#-system-architecture)
* [End-to-End Workflow](#-end-to-end-workflow)
* [AI Agent Architecture](#-ai-agent-architecture)
* [Agent Responsibilities](#-agent-responsibilities)
* [Market Agent](#-market-agent)
* [Geographic Agent](#-geographic-agent)
* [Competition Agent](#-competition-agent)
* [Financial Agent](#-financial-agent)
* [Opportunity Agent](#-opportunity-agent)
* [SWOT Agent](#-swot-agent)
* [Final Report](#-final-report)
* [Financial Architecture](#-financial-architecture)
* [External Data Architecture](#-external-data-architecture)
* [Government Scheme Data](#-government-scheme-data)
* [Technology Stack](#-technology-stack)
* [Repository Structure](#-repository-structure)
* [Backend Architecture](#-backend-architecture)
* [Frontend Architecture](#-frontend-architecture)
* [API Architecture](#-api-architecture)
* [Database Architecture](#-database-architecture)
* [Multilingual Chatbot](#-multilingual-chatbot)
* [Security Considerations](#-security-considerations)
* [Testing Strategy](#-testing-strategy)
* [Configuration](#-configuration)
* [Development Roadmap](#-development-roadmap)
* [Documentation](#-documentation)
* [Current Limitations](#-current-limitations)
* [Future Scope](#-future-scope)
* [License](#-license)

---

# 🌱 Overview

Small and emerging entrepreneurs often need to evaluate several factors before starting a business:

* Is there sufficient demand?
* Is the selected location suitable?
* Who are the competitors?
* What pricing conditions exist?
* What are the relevant market conditions?
* How much investment is required?
* How much financing may be required?
* What government schemes may be relevant?
* What opportunities exist?
* What are the major strengths and weaknesses?
* What risks should be considered?

GraminAI is designed to bring these analyses together into a single structured workflow. The planned platform accepts business information from the user and generates a structured feasibility report.

```text
Business Information
        │
        ▼
┌─────────────────────────────────────────┐
│     FOUR INDEPENDENT FIRST-LEVEL        │
│             AGENTS                      │
│ Market / Geographic / Competition /     │
│ Financial                               │
└────────────────────┬────────────────────┘
                     │
              Wait for all 4
                     │
                     ▼
              Opportunity → SWOT → Final Report
```

---

# 🎯 Problem Statement

Entrepreneurs in rural and semi-urban areas may need to collect information from multiple sources before evaluating a business idea: market information, geographic/location services, competitor/place data, government datasets and scheme sources, and deterministic financial calculations.

GraminAI is designed to provide a unified workflow that combines these sources and produces structured business analysis, including multilingual interaction.

---

# 🎯 Goals

The planned system aims to:

* Provide structured business feasibility analysis.
* Analyze market conditions, geographic suitability, and competition.
* Perform deterministic financial calculations and interpret financing/scheme information.
* Identify opportunities and generate SWOT plus a consolidated report.
* Support multilingual interaction.
* Maintain structured workflow state.
* Separate external data retrieval from AI reasoning.
* Support multiple external data providers through abstractions.

---

# 🚀 Planned Features

## 📊 Business Feasibility Analysis

The user will provide information such as business type, location, budget, own investment, loan requirement, target market, and language.

Example:

```json
{
  "business": "Dairy Farm",
  "location": "Mysuru",
  "budget": 500000,
  "own_investment": 150000,
  "loan_required": 350000,
  "language": "kn"
}
```

The request is validated by FastAPI/Pydantic and passed to the feasibility workflow.

---

# 🏗️ System Architecture

```text
USER → Next.js / React → HTTPS REST → FastAPI → Pydantic → Feasibility Service
  → LangGraph / LangChain orchestrator
  → Market | Geographic | Competition | Financial   (parallel, independent)
  → wait for all 4 → Opportunity → wait for 5 → SWOT → Final report
  → FastAPI → Next.js → USER
```

---

# 🤖 AI Agent Architecture

**Important:** The Financial Agent is **not downstream of Market, Geographic, or Competition**. It is a separate first-level branch. All four place results into shared workflow state.

---

# 🔄 End-to-End Workflow

```text
Market ─────────────┐
Geographic ─────────┤
Competition ────────┤
Financial ──────────┘
          │
          ▼
     Wait for all 4
          │
          ▼
     Opportunity
          │
          ▼
        SWOT
          │
          ▼
    Final Report
```

---

# 🧠 Agent Responsibilities

| Agent | Responsibility | Data source | Depends on |
| --- | --- | --- | --- |
| **Market Agent** | Demand indicators, customers, pricing, market conditions (analysis) | data.gov.in / AGMARKNET via `DataGovMarketDataProvider` (prices only) | User input |
| **Geographic Agent** | Location suitability, accessibility, proximity | Google Geocoding, Places (New), Routes | User input |
| **Competition Agent** | Competitors, competitive factors (not revenue/market share) | Google Places API (New) | User input |
| **Financial Agent** | Calculator + scheme interpretation | Official sources → PostgreSQL + Python calculator | User financial input |
| **Opportunity Agent** | Opportunities from combined analysis | Workflow state | First 4 agents |
| **SWOT Agent** | Strengths, weaknesses, opportunities, threats | Workflow state | First 4 + Opportunity |
| **Final Report** | Consolidate analysis | Workflow state | Previous results |

---

# 📊 Market Agent

Observed data: commodity, mandi, min/max/modal price, date. Demand is **inference**, not an AGMARKNET field.

```text
Orchestrator → Market Agent → DataGovMarketDataProvider → data.gov.in / AGMARKNET
  → context (user + prices) → LLMProvider → OpenRouter → MarketAnalysis → state
```

---

# 📍 Geographic Agent

Coordinates and distances come from Google APIs, not the LLM.

```text
Geographic Agent → GoogleMapsGeographicDataProvider
  ├── Geocoding API → lat/lng / Place ID
  ├── Places API (New) → nearby / text search / details
  └── Routes API → distance / duration
  → context → OpenRouter → GeographicAnalysis
```

---

# 🏪 Competition Agent

```text
Competition Agent → GooglePlacesCompetitionProvider → Places API (New)
  (Text Search / Nearby Search / Place Details)
  → competitors → OpenRouter → CompetitionAnalysis
```

Google Places does **not** provide competitor revenue, profit, market share, or exact product pricing.

---

# 💰 Financial Agent

The Financial Agent is a first-level independent agent. It does **not** wait for Market, Geographic, or Competition.

```text
Financial Agent
  ├── Government sources → ingest → PostgreSQL → GovernmentSchemeProvider
  ├── Python FinancialCalculator (authoritative EMI / interest / repayment)
  └── OpenRouter (interpretation only)
```

There is **no** fictional single Government Loan API.

---

# 💡 Opportunity Agent

Starts only after the four first-level analyses exist. It does not repeat market, maps, places, or government HTTP.

---

# 🧩 SWOT Agent

Waits for Market, Geographic, Competition, Financial, **and** Opportunity.

```json
{
  "strengths": [],
  "weaknesses": [],
  "opportunities": [],
  "threats": []
}
```

---

# 📄 Final Report

Python aggregation and/or a report agent. If an LLM is used, it must not alter EMI, total interest, total repayment, official loan limits, subsidy, or eligibility. See `lock_authoritative_finance` in `apps/api`.

---

# 💰 Financial Architecture

Python owns numerical correctness. Official sources own scheme facts. The LLM explains them.

---

# 🌐 External Data Architecture

```text
Agent → Data Provider → External source → Current data → Agent context → OpenRouter → LLM → Structured analysis
```

---

# 🏛️ Government Scheme Data

```text
data.gov.in / official Ministry / State / JanSamarth (adapter boundary)
  → ingestion → PostgreSQL → GovernmentSchemeProvider → Financial Agent
```

JanSamarth is **not** assumed to expose a generic public API.

---

# 🛠️ Technology Stack

| Layer | Choice |
| --- | --- |
| Frontend | Next.js, React, TypeScript |
| Backend | Python, FastAPI, Pydantic |
| Orchestration | LangGraph / LangChain (architecture) |
| LLM gateway | OpenRouter `POST https://openrouter.ai/api/v1/chat/completions` |
| Database | PostgreSQL (planned persistence) |

---

# 📁 Repository Structure

```text
graminai/
├── apps/web/          Next.js
├── apps/api/          FastAPI, agents, providers, calculator, workflow
├── packages/          Shared TS types and JSON Schema contracts
├── docs/              Architecture, providers, API, decisions
├── scripts/
├── .env.example
├── .gitignore
└── README.md
```

---

# ⚙️ Backend Architecture

```text
FastAPI → routes → Pydantic → FeasibilityService → LangGraph workflow
  → agents / calculator / providers → repositories → PostgreSQL
```

Routes do not contain agent or calculator logic.

---

# 🖥️ Frontend Architecture

Next.js talks **only** to FastAPI over HTTPS. Typed client: `apps/web/lib/api.ts`. Hook: `apps/web/hooks/useFeasibility.ts`. No `NEXT_PUBLIC_` OpenRouter, Google, or data.gov.in keys.

---

# 🌐 API Architecture

```text
GET  /health
POST /api/v1/feasibility
```

Planned later: chat, financial calculate, GET-by-id, conversations.

Internal orchestrator/agent calls are not HTTP.

---

# 🗄️ Database Architecture

Normalized scheme tables live in `apps/api/app/database/models.py`. Agents never open PostgreSQL; they use `GovernmentSchemeProvider`.

---

# 💬 Multilingual Chatbot

Planned: Next.js chat UI → FastAPI chat service → OpenRouter. Exact money questions should use the Python calculator, not LLM arithmetic.

---

# 🔐 Security Considerations

```text
❌ Next.js → OpenRouter / Google / data.gov.in
✅ Next.js → FastAPI → providers
```

Never commit real credentials.

---

# 🧪 Testing Strategy

```bash
cd apps/api && pytest
python scripts/check_imports.py
```

Tests cover schemas, calculator, workflow barriers, provider isolation, EMI lock on final report, and health/feasibility routes. Default feasibility uses **mock providers** so the API can run without keys.

---

# ⚙️ Configuration

See `.env.example`:

```env
OPENROUTER_API_KEY=
OPENROUTER_MODEL=
GOOGLE_MAPS_API_KEY=
DATA_GOV_IN_API_KEY=
DATABASE_URL=
MARKET_DATA_PROVIDER=datagov
GEOGRAPHIC_DATA_PROVIDER=google_maps
COMPETITION_DATA_PROVIDER=google_places
GOVERNMENT_DATA_PROVIDER=government_sources
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

# 🗺️ Development Roadmap

## Phase 1 — Architecture & Scaffolding

* [x] Overall architecture and monorepo
* [x] Agent dependency architecture
* [x] Documentation

## Later phases (production)

* [ ] Live data.gov.in, Google, and OpenRouter HTTP
* [ ] PostgreSQL + scheme ingestion
* [ ] Production prompts
* [ ] Polished Next.js UI and chatbot
* [ ] Auth and deployment

---

# 📚 Documentation

```text
docs/architecture/   overview, diagrams, audit, database, remaining
docs/providers/      market, geographic, competition, financial, openrouter
docs/api/            feasibility
docs/decisions/      ADRs
```

---

# ⚠️ Current Limitations

Intentional in this phase: no live vendor HTTP, no invented mandi/Places rows presented as production data, no polished UI, no auth.

---

# 🔮 Future Scope

More languages and categories, additional providers, richer financial models, scheme sync, user profiles, report export, observability, production deployment.

---

# 📊 Project Status

```text
Architecture        ████████████████████  scaffolding
Contracts           ████████████░░░░░░░░  typed + mocks
Live external APIs  ░░░░░░░░░░░░░░░░░░░░  not implemented
Polished product    ░░░░░░░░░░░░░░░░░░░░  not implemented
```

---

# 🧭 Core Architecture Principle

**Financial Agent is beside Market, Geographic, and Competition — not below them.**

The four first-level agents only become connected when their structured results enter shared workflow state. Then Opportunity, then SWOT, then the final report.

---

# 📄 License

This project is currently under development. Add an open-source license before public distribution if required.

---

## Local run

```bash
cd apps/api
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# from repo root
npm install
npm run web
```

**Current Status: Architecture & Scaffolding Phase**
