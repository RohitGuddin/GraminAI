# OpenRouter

```
Agent → LLMProvider → OpenRouterLLMProvider
  → POST https://openrouter.ai/api/v1/chat/completions
  → LLM JSON Schema
  → Pydantic validation
```

Auth: `Authorization: Bearer OPENROUTER_API_KEY`.

The LLM does not fetch mandi, Maps, or scheme HTTP itself. Agents retrieve data first.

Live HTTP raises a 501-style provider error in this phase. Tests use `MockLLMProvider`.
