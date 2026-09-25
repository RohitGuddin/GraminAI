# System architecture

**Status:** architecture / scaffolding.

```
USER → Next.js → HTTPS REST → FastAPI → Pydantic → Feasibility Service
  → LangGraph orchestrator
  → Market | Geographic | Competition | Financial  (parallel)
  → wait 4 → Opportunity → wait 5 → SWOT → Final report
  → FastAPI → Next.js → USER
```

See [diagrams.md](./diagrams.md) for Mermaid.

## Layers

- **apps/web**: UI, forms later, typed client. No provider API keys.
- **apps/api**: routes, services, workflow, agents, providers, calculator, repositories.

## Parallelism

First-level agents do not read each other's outputs. `LangGraphWorkflow.run_async` runs them with `asyncio.gather` on deep copies, then merges keys.
