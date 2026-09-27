# 🌾 GraminAI

### Multilingual AI-Powered Business Advisory Platform for Rural & Semi-Urban Entrepreneurs

GraminAI is a planned multilingual AI business advisory platform designed to help rural and semi-urban entrepreneurs evaluate business opportunities through structured **market, geographic, competition, financial, opportunity, and SWOT analysis**.

The system is designed around a LangChain-based workflow containing four independent first-level analysis agents:

* Market Agent
* Geographic Agent
* Competition Agent
* Financial Agent

These agents produce structured results independently. Once all four results are available, the workflow passes them to the Opportunity Agent. The SWOT Agent then consumes the four first-level analyses together with the Opportunity analysis before the final report is generated.

> **Current Status:** Architecture & Scaffolding Phase
> This repository currently focuses on system architecture, project structure, workflow design, schemas, interfaces, and documentation. Production implementation of the AI agents, external data providers, financial engine, database persistence, APIs, chatbot, and frontend workflows will be developed in subsequent phases.

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

GraminAI is designed to bring these different analyses together into a single structured workflow.

The planned platform will accept business information from the user and generate a structured feasibility report.

```text
Business Information
        │
        ▼
┌─────────────────────────────────────────┐
│     FOUR INDEPENDENT FIRST-LEVEL        │
│             AGENTS                      │
│                                         │
│ Market                                  │
│ Geographic                              │
│ Competition                             │
│ Financial                               │
└────────────────────┬────────────────────┘
                     │
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

# 🎯 Problem Statement

Entrepreneurs in rural and semi-urban areas may need to collect information from multiple sources before evaluating a business idea.

Relevant information can be distributed across:

* market information
* geographic/location services
* business and competitor information
* government datasets
* government scheme sources
* financial calculations
* other relevant data sources

GraminAI is designed to provide a unified workflow that combines these sources and produces structured business analysis.

The platform is also designed to support multilingual interaction.

---

# 🎯 Goals

The planned system aims to:

* Provide structured business feasibility analysis.
* Analyze market conditions.
* Analyze geographic suitability.
* Analyze competition.
* Perform deterministic financial calculations.
* Analyze financing requirements.
* Identify relevant government scheme information.
* Identify business opportunities.
* Generate SWOT analysis.
* Generate a consolidated feasibility report.
* Support multilingual interaction.
* Maintain structured workflow state.
* Separate external data retrieval from AI reasoning.
* Keep exact financial calculations deterministic.
* Support multiple external data providers through abstractions.

---

# 🚀 Planned Features

## 📊 Business Feasibility Analysis

The user will provide information such as:

```text
Business Type
Location
Budget
Own Investment
Loan Requirement
Target Market
Language
```

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

The request will eventually be validated by FastAPI/Pydantic and passed to the feasibility workflow.

---

# 🤖 AI Agent Architecture

GraminAI contains **four independent first-level agents**.

```text
                         ┌──────────────────────┐
                         │ LangChain            │
                         │ Orchestrator         │
                         └──────────┬───────────┘
                                    │
            ┌───────────────────────┼───────────────────────┐
            │                       │                       │
            │                       │                       │
            ▼                       ▼                       ▼
      ┌───────────┐          ┌────────────┐          ┌──────────────┐
      │  Market   │          │ Geographic │          │ Competition  │
      │   Agent   │          │   Agent    │          │    Agent     │
      └─────┬─────┘          └─────┬──────┘          └──────┬───────┘
            │                      │                        │
            │                      │                        │
            │                      │                        │
            └──────────────────────┼────────────────────────┘
                                   │
                          ┌────────▼────────┐
                          │ Financial Agent │
                          └────────┬─────────┘
                                   │
                                   │
                         All four are independent
                         first-level analyses
                                   │
                                   ▼
                         ┌──────────────────┐
                         │ LangChain State  │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Opportunity     │
                         │ Agent            │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ SWOT Agent       │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Final Report     │
                         └──────────────────┘
```

**Important:** The Financial Agent is **not downstream of Market, Geographic, or Competition**. It is a separate first-level branch.

The first four agents can execute independently and their results are then placed into shared workflow state.

---

# 🔄 End-to-End Workflow

```text
                                      ┌───────────────┐
                                      │     USER      │
                                      │               │
                                      │ Kannada /     │
                                      │ Hindi / Tamil │
                                      │ Telugu /      │
                                      │ English / etc.│
                                      └───────┬───────┘
                                              │
                                              │ Original Input
                                              ▼
                              ┌─────────────────────────┐
                              │     Next.js / React     │
                              │                         │
                              │ • UI / Forms / Chat     │
                              │ • Collect user input    │
                              │ • Preserve original    │
                              │   language              │
                              └───────────┬─────────────┘
                                          │
                                          │ HTTPS REST
                                          ▼
                              ┌─────────────────────────┐
                              │         FastAPI         │
                              │                         │
                              │ • API boundary         │
                              │ • Authentication       │
                              │ • Authorization        │
                              └───────────┬─────────────┘
                                          │
                                          ▼
                              ┌─────────────────────────┐
                              │   Pydantic Validation   │
                              │                         │
                              │ Validate request schema │
                              └───────────┬─────────────┘
                                          │
                                          ▼
                              ┌─────────────────────────┐
                              │    Feasibility Service  │
                              │                         │
                              │ Main business workflow  │
                              └───────────┬─────────────┘
                                          │
                                          ▼
                    ┌────────────────────────────────────────────┐
                    │   LANGUAGE PROCESSING / TRANSLATION LAYER │
                    │                                            │
                    │ • Detect / identify language               │
                    │ • Preserve original input                  │
                    │ • Translate / normalize                    │
                    │ • Extract structured business information  │
                    │                                            │
                    │ Can use:                                   │
                    │   • Multilingual LLM                        │
                    │   • Translation API / Service               │
                    └──────────────────────┬─────────────────────┘
                                           │
                                           │
                         ┌─────────────────┴─────────────────┐
                         │                                   │
                         ▼                                   ▼
              ┌─────────────────────┐             ┌─────────────────────┐
              │  Multilingual LLM   │             │ Translation API /  │
              │                     │             │ Translation Model   │
              │ Through OpenRouter  │             │                     │
              │ if selected         │             │ if selected         │
              └──────────┬──────────┘             └──────────┬──────────┘
                         │                                   │
                         └─────────────────┬─────────────────┘
                                           │
                                           ▼
                         ┌────────────────────────────────┐
                         │ Normalized Business Context    │
                         │                                │
                         │ original_input                 │
                         │ original_language              │
                         │ normalized_text                │
                         │ business_type                  │
                         │ location                       │
                         │ budget                         │
                         │ loan_required                  │
                         │ experience                     │
                         │ target_market                  │
                         └───────────────┬────────────────┘
                                         │
                                         ▼
                              ┌─────────────────────────┐
                              │   Pydantic Validation   │
                              │                         │
                              │ Validate normalized     │
                              │ structured output       │
                              └───────────┬─────────────┘
                                          │
                                          ▼
                              ┌─────────────────────────┐
                              │      Workflow State     │
                              │                         │
                              │ • Request ID            │
                              │ • Original input        │
                              │ • Language              │
                              │ • Business context      │
                              │ • Agent results         │
                              └───────────┬─────────────┘
                                          │
                                          ▼
                              ┌─────────────────────────┐
                              │  LangChain Orchestrator │
                              │                         │
                              │ Controls workflow and   │
                              │ agent execution/state   │
                              └───────────┬─────────────┘
                                          │
                    ┌─────────────────────┼─────────────────────┐
                    │                     │                     │
                    ▼                     ▼                     ▼
           ┌────────────────┐    ┌────────────────┐    ┌────────────────┐
           │  Market Agent  │    │  Geographic    │    │  Competition   │
           │                │    │     Agent      │    │     Agent      │
           │ • Demand       │    │ • Location     │    │ • Competitors  │
           │ • Customers    │    │ • Suitability  │    │ • Pricing      │
           │ • Trends       │    │ • Infrastructure│   │ • Positioning  │
           └───────┬────────┘    └───────┬────────┘    └───────┬────────┘
                   │                     │                     │
                   │                     │                     │
                   │                     │                     │
                   │             ┌───────▼────────┐            │
                   │             │ Financial Agent │            │
                   │             │                 │            │
                   │             │ • Investment    │            │
                   │             │ • Loan          │            │
                   │             │ • Revenue       │            │
                   │             │ • Costs         │            │
                   │             │ • Cash Flow     │            │
                   │             │ • Schemes       │            │
                   │             └───────┬─────────┘            │
                   │                     │                      │
                   └─────────────────────┼──────────────────────┘
                                         │
                                         │
                              FOUR AGENTS ARE INDEPENDENT
                                         │
                                         ▼
                              ┌─────────────────────────┐
                              │      LangChain State    │
                              │                         │
                              │ Wait for all required   │
                              │ first-level agent       │
                              │ results                 │
                              └───────────┬─────────────┘
                                          │
                                          ▼
                              ┌─────────────────────────┐
                              │    Opportunity Agent    │
                              │                         │
                              │ Consumes:               │
                              │ • Market                │
                              │ • Geographic            │
                              │ • Competition           │
                              │ • Financial             │
                              │                         │
                              │ Identifies business     │
                              │ opportunities and       │
                              │ constraints              │
                              └───────────┬─────────────┘
                                          │
                                          ▼
                              ┌─────────────────────────┐
                              │      LangChain State    │
                              │                         │
                              │ Store Opportunity       │
                              │ analysis                │
                              └───────────┬─────────────┘
                                          │
                                          │ Required input available
                                          ▼
                              ┌─────────────────────────┐
                              │        SWOT Agent       │
                              │                         │
                              │ • Strengths             │
                              │ • Weaknesses            │
                              │ • Opportunities         │
                              │ • Threats               │
                              └───────────┬─────────────┘
                                          │
                                          ▼
                              ┌─────────────────────────┐
                              │       Final Report      │
                              │                         │
                              │ • Market analysis       │
                              │ • Geographic analysis   │
                              │ • Competition analysis  │
                              │ • Financial analysis    │
                              │ • Opportunity analysis  │
                              │ • SWOT                   │
                              └───────────┬─────────────┘
                                          │
                                          ▼
                              ┌─────────────────────────┐
                              │   Response Localization │
                              │                         │
                              │ Convert/adapt the final │
                              │ explanation into the    │
                              │ user's preferred or     │
                              │ original language       │
                              │                         │
                              │ Can use:                │
                              │ • LLM                   │
                              │ • Translation API       │
                              └───────────┬─────────────┘
                                          │
                                          ▼
                              ┌─────────────────────────┐
                              │         FastAPI         │
                              │                         │
                              │ Final API response      │
                              └───────────┬─────────────┘
                                          │
                                          │ JSON
                                          ▼
                              ┌─────────────────────────┐
                              │     Next.js / React     │
                              │                         │
                              │ Render final report     │
                              └───────────┬─────────────┘
                                          │
                                          ▼
                                      ┌───────┐
                                      │ USER  │
                                      │       │
                                      │ Final │
                                      │ result│
                                      │ in    │
                                      │ chosen│
                                      │language│
                                      └───────┘
```

The intended execution sequence is explicitly:

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
     Wait for required data
          │
          ▼
        SWOT
          │
          ▼
    Final Report
```

---

# 🧠 Agent Responsibilities

| Agent                 | Responsibility                                           | Data Source                                         | Depends On                    |
| --------------------- | -------------------------------------------------------- | --------------------------------------------------- | ----------------------------- |
| **Market Agent**      | Demand, customers, pricing, market conditions            | Market/data provider                                | User input                    |
| **Geographic Agent**  | Location suitability, accessibility, proximity           | Geographic/location provider                        | User input                    |
| **Competition Agent** | Competitors, pricing pressure, differentiation           | Business/place provider                             | User input + relevant context |
| **Financial Agent**   | Financial calculations, financing, scheme interpretation | Government sources + PostgreSQL + Python calculator | User financial input          |
| **Opportunity Agent** | Identify opportunities from combined analysis            | Previous agent outputs                              | First 4 agents                |
| **SWOT Agent**        | Strengths, weaknesses, opportunities, threats            | Previous agent outputs                              | First 4 + Opportunity         |
| **Final Report**      | Consolidate complete analysis                            | Workflow state                                      | Previous results              |

---

# 📊 Market Agent

The Market Agent is a first-level independent agent.

```text
                LangChain Orchestrator
                         │
                         ▼
                  Market Agent
                         │
                         ▼
                Market Data Provider
                         │
                         ▼
                 Current Market Data
                         │
                         ▼
              User Business Information
                         +
                  Current Data
                         │
                         ▼
                  Context Builder
                         │
                         ▼
                    OpenRouter
                         │
                         ▼
                        LLM
                         │
                         ▼
               Market Analysis
                         │
                         ▼
                  LangChain State
```

Potential output:

```text
MarketAnalysis
├── demand_indicators
├── target_customers
├── pricing_conditions
├── market_conditions
└── challenges
```

The architecture deliberately does not assume a specific market API until an actual provider is selected.

---

# 📍 Geographic Agent

The Geographic Agent is also a first-level independent agent.

```text
                LangChain Orchestrator
                         │
                         ▼
                Geographic Agent
                         │
                         ▼
             Geographic Data Provider
                         │
                         ▼
             Current Location Data
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
          Location   Coordinates  Nearby Data
              │          │          │
              └──────────┼──────────┘
                         │
                         ▼
                   Context Builder
                         │
                         ▼
                     OpenRouter
                         │
                         ▼
                        LLM
                         │
                         ▼
              Geographic Analysis
                         │
                         ▼
                  LangChain State
```

Potential output:

```text
GeographicAnalysis
├── location
├── location_suitability
├── accessibility
├── customer_proximity
├── supplier_access
└── constraints
```

The source architecture describes geographic/location providers as supplying current geographic information before LLM analysis.

---

# 🏪 Competition Agent

The Competition Agent is another independent first-level agent.

```text
                LangChain Orchestrator
                         │
                         ▼
                Competition Agent
                         │
                         ▼
            Competition Data Provider
                         │
                         ▼
              Competitor Information
                         │
                         ├──────────────┐
                         ▼              ▼
                  Business Data    Market Context
                         │              │
                         └──────┬───────┘
                                │
                                ▼
                         Context Builder
                                │
                                ▼
                            OpenRouter
                                │
                                ▼
                               LLM
                                │
                                ▼
                    Competition Analysis
                                │
                                ▼
                         LangChain State
```

Potential output:

```text
CompetitionAnalysis
├── competition_level
├── competitors
├── pricing_pressure
├── competitive_factors
├── differentiation_opportunities
└── market_gaps
```

The source architecture similarly separates competitor data retrieval from the subsequent LLM analysis.

---

# 💰 Financial Agent

## Important Architectural Point

The **Financial Agent is a first-level independent agent**.

It does **not** wait for Market, Geographic, or Competition.

Its input comes from:

* user financial information
* government scheme information
* financial data
* deterministic Python calculations

Its result is placed into the same LangChain workflow state as the other three first-level agents.

```text
                    LangChain Orchestrator
                              │
                              ▼
                     ┌────────────────┐
                     │ Financial Agent│
                     └───────┬────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
   Government Sources     PostgreSQL      Python Calculator
          │                  │                  │
          │                  │                  │
          ▼                  ▼                  ▼
   Scheme Information   Stored Data      Exact Calculations
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
                             ▼
                    Financial Context
                             │
                             ▼
                        OpenRouter
                             │
                             ▼
                            LLM
                             │
                             ▼
                  Financial Analysis
                             │
                             ▼
                      LangChain State
```

The Financial Agent's architecture is separate from the other three agents, while all four ultimately contribute to shared workflow state.

### Deterministic Financial Calculation

```text
User Financial Inputs
        │
        ▼
Python Financial Calculator
        │
        ├── EMI
        ├── Interest
        ├── Total Repayment
        ├── Repayment Schedule
        └── Other Calculations
        │
        ▼
Exact Financial Values
        │
        ▼
Financial Agent
        │
        ▼
OpenRouter / LLM
        │
        ▼
Financial Interpretation
```

The LLM should interpret the calculated values rather than independently generating authoritative EMI or interest calculations.

---

# 💡 Opportunity Agent

The Opportunity Agent is a **downstream dependent agent**.

It starts only after the four first-level analyses are available.

```text
Market Analysis
       │
Geographic Analysis
       │
Competition Analysis
       │
Financial Analysis
       │
       └──────────────┐
                      ▼
               LangChain State
                      │
                      ▼
             Opportunity Agent
                      │
                      ▼
                OpenRouter
                      │
                      ▼
                     LLM
                      │
                      ▼
           Opportunity Analysis
                      │
                      ▼
              LangChain State
```

Potential output:

```text
OpportunityAnalysis
├── opportunities
│   ├── title
│   ├── reason
│   └── supporting_factors
└── risks / conditions
```

The Opportunity Agent does not need to repeat the external API calls already performed by the first-level agents.

---

# 🧩 SWOT Agent

The SWOT Agent is downstream from Opportunity.

It waits until all five required analyses are available:

```text
Market
Geographic
Competition
Financial
Opportunity
       │
       ▼
LangChain State
       │
       ▼
SWOT Agent
       │
       ▼
OpenRouter
       │
       ▼
LLM
       │
       ▼
SWOT Analysis
```

Output:

```json
{
  "strengths": [],
  "weaknesses": [],
  "opportunities": [],
  "threats": []
}
```

The source workflow explicitly defines SWOT as depending on Market, Geographic, Competition, Financial, and Opportunity results.

---

# 📄 Final Report

After SWOT is completed, the workflow has the structured analysis required to produce the final feasibility report.

```text
Market Analysis
       │
Geographic Analysis
       │
Competition Analysis
       │
Financial Analysis
       │
Opportunity Analysis
       │
SWOT Analysis
       │
       ▼
LangChain State
       │
       ▼
Final Report Generation
       │
       ├───────────────┐
       │               │
       ▼               ▼
Python Aggregation   Report Agent
                         │
                         ▼
                    OpenRouter
                         │
                         ▼
                        LLM
       │               │
       └───────┬───────┘
               ▼
        Final Structured Report
               │
               ▼
             FastAPI
               │
               ▼
            Next.js
               │
               ▼
              USER
```

The architecture can support either deterministic aggregation or a final LLM synthesis layer. If an LLM is used, exact financial and official eligibility information must be preserved.

---

# 💰 Financial Architecture

Financial calculations are intentionally separated from LLM reasoning.

```text
              Financial Agent
                     │
       ┌─────────────┼─────────────┐
       │             │             │
       ▼             ▼             ▼
 Government      PostgreSQL    Python Calculator
   Sources          Data              │
       │             │                │
       └─────────────┼────────────────┘
                     │
                     ▼
             Financial Context
                     │
                     ▼
                 OpenRouter
                     │
                     ▼
                    LLM
                     │
                     ▼
          Financial Interpretation
```

The Python calculator is responsible for exact calculations such as:

* EMI
* interest
* total repayment
* repayment schedule
* other deterministic financial calculations

The LLM provides interpretation and explanation.

---

# 🌐 External Data Architecture

The architecture does not assume that every agent has a dedicated API.

Instead, external data is accessed through provider abstractions.

```text
                     Agent
                       │
                       ▼
                Data Provider
                       │
                       ▼
              External Data Source
                       │
                       ▼
                 Current Data
                       │
                       ▼
               Agent Context
                       │
                       ▼
                  OpenRouter
                       │
                       ▼
                      LLM
                       │
                       ▼
             Structured Analysis
```

Potential categories include:

* Market data
* Geographic/location data
* Business/place data
* Government datasets
* Official scheme sources

Specific providers and endpoints are implementation decisions and should not be invented during the architecture phase.

---

# 🏛️ Government Scheme Data

Government scheme information is designed around multiple official sources rather than assuming one universal government loan API.

```text
              Government Information
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      data.gov.in   Official     State Govt.
                    Sources       Sources
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
                 Data Ingestion
                       │
                       ▼
                   PostgreSQL
                       │
                       ▼
          Government Scheme Provider
                       │
                       ▼
                Financial Agent
```

PostgreSQL therefore acts as a normalized internal source for synchronized government information where appropriate.

---

# 🛠️ Technology Stack

## Frontend

* Next.js
* React
* TypeScript

Responsibilities:

* User interface
* Forms
* Business information collection
* Feasibility report visualization
* Financial result visualization
* SWOT visualization
* Chatbot interface
* API communication

---

## Backend

* Python
* FastAPI
* Pydantic

Responsibilities:

* REST APIs
* Request validation
* Application services
* Workflow invocation
* Response handling
* Error handling

---

## AI

* LangChain
* OpenRouter
* LLMs

### LangChain

Responsible for:

* workflow orchestration
* structured state
* agent coordination
* dependency management

### OpenRouter

Responsible for:

* LLM gateway/provider access

### LLM

Responsible for:

* analysis
* reasoning
* interpretation
* structured natural-language generation

---

## Database

* PostgreSQL

Planned responsibilities:

* feasibility results
* conversations
* chat messages
* workflow/request metadata
* government scheme information
* synchronized official data

---

# 📁 Repository Structure

```text
graminai/
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── services/
│   ├── types/
│   └── ...
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   └── dependencies/
│   │   │
│   │   ├── core/
│   │   │   ├── config/
│   │   │   └── logging/
│   │   │
│   │   ├── schemas/
│   │   │
│   │   ├── services/
│   │   │
│   │   ├── domain/
│   │   │
│   │   ├── ai/
│   │   │   ├── orchestrator/
│   │   │   ├── agents/
│   │   │   │   ├── market/
│   │   │   │   ├── geographic/
│   │   │   │   ├── competition/
│   │   │   │   ├── financial/
│   │   │   │   ├── opportunity/
│   │   │   │   └── swot/
│   │   │   │
│   │   │   ├── providers/
│   │   │   └── prompts/
│   │   │
│   │   ├── financial/
│   │   │
│   │   ├── db/
│   │   │
│   │   ├── repositories/
│   │   │
│   │   └── ...
│   │
│   └── tests/
│
├── docs/
│   ├── architecture.md
│   ├── ai-architecture.md
│   ├── workflow.md
│   ├── data-sources.md
│   ├── financial-engine.md
│   ├── database.md
│   ├── api.md
│   ├── frontend.md
│   └── agents/
│       ├── market.md
│       ├── geographic.md
│       ├── competition.md
│       ├── financial.md
│       ├── opportunity.md
│       ├── swot.md
│       └── final-report.md
│
├── scripts/
│
├── .env.example
├── .gitignore
├── README.md
└── LICENSE
```

---

# ⚙️ Backend Architecture

```text
                  FastAPI
                     │
                     ▼
             API / Route Layer
                     │
                     ▼
            Pydantic Validation
                     │
                     ▼
           Application Services
                     │
                     ▼
          LangChain Orchestrator
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
      Agents     Financial     Providers
                   Engine
        │            │            │
        └────────────┼────────────┘
                     │
                     ▼
               Repositories
                     │
                     ▼
                 PostgreSQL
```

The API layer should not contain the core AI or financial business logic.

---

# 🌐 API Architecture

Planned endpoints include:

```text
POST /api/v1/feasibility

POST /api/v1/chat

POST /api/v1/financial/calculate

GET /api/v1/feasibility/{request_id}

GET /api/v1/conversations/{conversation_id}
```

The feasibility request flow is:

```text
Next.js
   │
   │ HTTPS POST
   ▼
FastAPI
   │
   ▼
Pydantic
   │
   ▼
Feasibility Service
   │
   ▼
LangChain Orchestrator
```

No HTTP API is required between the internal FastAPI service, orchestrator, and agents. Those are internal application components. The uploaded workflow explicitly distinguishes the external HTTPS calls from these internal Python/component interactions.

---

# 🗄️ Database Architecture

Planned PostgreSQL entities may include:

```text
User
 │
 ├── FeasibilityRequest
 │        │
 │        └── FeasibilityResult
 │
 └── Conversation
          │
          └── ChatMessage
```

Government scheme information:

```text
Official Sources
      │
      ▼
Data Ingestion
      │
      ▼
PostgreSQL
      │
      ▼
GovernmentSchemeProvider
      │
      ▼
Financial Agent
```

Agents should not directly manage database connections.

The intended separation is:

```text
Agent
  ↓
Service / Provider
  ↓
Repository
  ↓
PostgreSQL
```

---

# 💬 Multilingual Chatbot

The planned chatbot architecture is:

```text
USER
 │
 ▼
Next.js Chat UI
 │
 ▼
FastAPI
 │
 ▼
Chat Service
 │
 ▼
Conversation Context
 │
 ▼
OpenRouter
 │
 ▼
LLM
 │
 ▼
Response
 │
 ▼
FastAPI
 │
 ▼
Next.js
 │
 ▼
USER
```

The chatbot is intended to support multilingual business and financial assistance.

For questions requiring exact financial calculations, the architecture should use the deterministic financial calculation layer rather than asking the LLM to calculate exact values.

---

# 🔐 Security Considerations

## API Keys

OpenRouter credentials remain on the backend.

```text
❌ Next.js → OpenRouter

✅ Next.js → FastAPI → OpenRouter
```

## Database Credentials

PostgreSQL credentials remain server-side.

## Environment Variables

Secrets should be provided through environment configuration.

## External Provider Credentials

External API credentials should not be exposed to frontend users.

## Input Validation

FastAPI/Pydantic should validate incoming requests.

## LLM Output

Structured validation should be applied to agent outputs.

## Financial Data

Exact financial values should originate from deterministic calculation logic.

---

# 🧪 Testing Strategy

## Backend

Planned tests:

* Pydantic schemas
* application services
* agents
* data providers
* financial calculations
* repositories
* API endpoints
* workflow orchestration

## Agent Tests

Each agent should eventually test:

```text
Input
 ↓
Provider Data
 ↓
Context
 ↓
LLM
 ↓
Structured Output
```

## Workflow Tests

The primary workflow should verify:

```text
Market ──────────┐
Geographic ──────┤
Competition ─────┤
Financial ───────┘
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

## End-to-End Tests

Eventually:

```text
User
 ↓
Next.js
 ↓
FastAPI
 ↓
LangChain
 ↓
4 First-Level Agents
 ↓
Opportunity
 ↓
SWOT
 ↓
Final Report
 ↓
FastAPI
 ↓
Next.js
```

---

# ⚙️ Configuration

Planned environment variables:

```env
# Backend
DATABASE_URL=

# OpenRouter
OPENROUTER_API_KEY=
OPENROUTER_MODEL=

# Frontend
NEXT_PUBLIC_API_BASE_URL=

# External provider credentials
# Added when actual providers are selected.
```

Never commit real credentials.

---

# 🗺️ Development Roadmap

## Phase 1 — Architecture & Scaffolding

* [x] Overall architecture
* [x] Monorepo structure
* [x] Frontend architecture
* [x] Backend architecture
* [x] AI architecture
* [x] Agent dependency architecture
* [x] Financial architecture
* [x] Database architecture
* [x] API architecture
* [x] Documentation structure

## Phase 2 — Contracts

* [ ] Pydantic request schemas
* [ ] Agent input/output schemas
* [ ] Workflow state
* [ ] Provider interfaces
* [ ] Financial contracts
* [ ] API contracts

## Phase 3 — Infrastructure

* [ ] PostgreSQL
* [ ] OpenRouter
* [ ] LangChain
* [ ] External data providers
* [ ] Repository layer

## Phase 4 — First-Level Agents

These four agents are independent:

* [ ] Market Agent
* [ ] Geographic Agent
* [ ] Competition Agent
* [ ] Financial Agent

## Phase 5 — Downstream Workflow

* [ ] LangChain Orchestrator
* [ ] Parallel first-level execution
* [ ] Wait for all four results
* [ ] Opportunity Agent
* [ ] SWOT Agent
* [ ] Final Report

## Phase 6 — Financial Engine

* [ ] Deterministic calculations
* [ ] EMI
* [ ] Interest
* [ ] Total repayment
* [ ] Repayment schedule
* [ ] Government scheme data

## Phase 7 — FastAPI

* [ ] Feasibility API
* [ ] Financial API
* [ ] Chat API
* [ ] Result retrieval
* [ ] Conversation retrieval

## Phase 8 — Next.js

* [ ] Business input form
* [ ] Feasibility UI
* [ ] Financial UI
* [ ] Market UI
* [ ] Geographic UI
* [ ] Competition UI
* [ ] Opportunity UI
* [ ] SWOT UI
* [ ] Final report UI
* [ ] Chatbot UI
* [ ] Multilingual support

## Phase 9 — Testing

* [ ] Unit tests
* [ ] Agent tests
* [ ] Workflow tests
* [ ] Financial tests
* [ ] API tests
* [ ] Frontend tests
* [ ] End-to-end tests

---

# 📚 Documentation

```text
docs/
│
├── architecture.md
├── ai-architecture.md
├── workflow.md
├── data-sources.md
├── financial-engine.md
├── database.md
├── api.md
├── frontend.md
│
└── agents/
    ├── market.md
    ├── geographic.md
    ├── competition.md
    ├── financial.md
    ├── opportunity.md
    ├── swot.md
    └── final-report.md
```

---

# ⚠️ Current Limitations

The current repository is in the architecture/scaffolding phase.

Therefore:

* AI agents may not yet be production implementations.
* External API providers have not necessarily been selected.
* Specific external API endpoints should not be assumed.
* OpenRouter integration may not yet be implemented.
* PostgreSQL persistence may not yet be implemented.
* Government data synchronization may not yet be implemented.
* Deterministic financial calculations may not yet be implemented.
* Multilingual chatbot functionality may not yet be implemented.
* Production authentication may not yet be implemented.
* Deployment configuration may not yet be finalized.

These limitations are intentional as part of the staged development approach.

---

# 🔮 Future Scope

Potential future improvements include:

* More regional languages
* Additional business categories
* More market-data providers
* More geographic intelligence
* Enhanced competitor discovery
* Additional financial models
* Government scheme synchronization
* User profiles
* Persistent conversations
* Report export
* Advanced observability
* Production deployment
* Performance optimization
* Additional AI analysis modules

---

# 📊 Project Status

```text
Architecture        ████████████████████ 100%
Scaffolding         ████████████████████ 100%

Contracts           ░░░░░░░░░░░░░░░░░░░░ Planned
First-Level Agents  ░░░░░░░░░░░░░░░░░░░░ Planned
Workflow            ░░░░░░░░░░░░░░░░░░░░ Planned
Financial Engine    ░░░░░░░░░░░░░░░░░░░░ Planned
Database            ░░░░░░░░░░░░░░░░░░░░ Planned
External APIs       ░░░░░░░░░░░░░░░░░░░░ Planned
REST APIs           ░░░░░░░░░░░░░░░░░░░░ Planned
Frontend            ░░░░░░░░░░░░░░░░░░░░ Planned
Chatbot             ░░░░░░░░░░░░░░░░░░░░ Planned
Testing             ░░░░░░░░░░░░░░░░░░░░ Planned
```

---

# 🧭 Core Architecture Principle

The most important workflow distinction in GraminAI is:

```text
                 LANGCHAIN ORCHESTRATOR
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
       ▼                  ▼                  ▼
     MARKET           GEOGRAPHIC        COMPETITION
     AGENT              AGENT              AGENT
       │                  │                  │
       │                  │                  │
       └──────────────────┼──────────────────┘
                          │
                    FINANCIAL AGENT
                          │
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
        All 4 independent       LangChain State
        first-level agents             │
                                      ▼
                               OPPORTUNITY AGENT
                                      │
                                      ▼
                                  SWOT AGENT
                                      │
                                      ▼
                                FINAL REPORT
```

**Financial Agent is beside Market, Geographic, and Competition — not below them.**

Its internal data sources are independent:

```text
Financial Agent
    │
    ├── Government Sources
    ├── PostgreSQL
    └── Python Calculator
```

The four first-level agents only become connected when their **structured results enter the shared LangChain workflow state**. This is the key dependency design of GraminAI.

---

# 📄 License

This project is currently under development.

Add the appropriate open-source license before public distribution.

---

## 🌾 GraminAI

**Multilingual AI-powered business advisory architecture for rural and semi-urban entrepreneurs.**

```text
Next.js
   +
FastAPI
   +
Pydantic
   +
LangChain
   +
OpenRouter
   +
Specialized AI Agents
   +
Deterministic Financial Engine
   +
PostgreSQL
```

**Current Status: Architecture & Scaffolding Phase**
