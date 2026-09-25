from app.providers.implementations.openrouter_llm import (
    OPENROUTER_CHAT_COMPLETIONS_URL,
    OpenRouterLLMProvider,
)
from app.schemas.market import MarketAnalysis


def test_openrouter_contract_has_real_url_and_schema() -> None:
    provider = OpenRouterLLMProvider("test-key", "test-model")
    assert OPENROUTER_CHAT_COMPLETIONS_URL == "https://openrouter.ai/api/v1/chat/completions"
    payload = provider.build_payload(
        system_prompt="sys",
        user_context="user",
        schema=MarketAnalysis,
    )
    assert payload["model"] == "test-model"
    assert payload["response_format"]["json_schema"]["name"] == "MarketAnalysis"
    assert provider.build_headers()["Authorization"] == "Bearer test-key"
