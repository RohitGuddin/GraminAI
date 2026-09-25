from typing import Any

from pydantic import BaseModel, TypeAdapter

from app.core.exceptions import ProviderNotImplementedError

OPENROUTER_CHAT_COMPLETIONS_URL = "https://openrouter.ai/api/v1/chat/completions"


class OpenRouterLLMProvider:
    """Adapter for OpenRouter chat completions. Live HTTP is not enabled in this phase."""

    def __init__(self, api_key: str, default_model: str) -> None:
        self._api_key = api_key
        self._default_model = default_model

    def build_headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }

    def build_payload(
        self,
        *,
        system_prompt: str,
        user_context: str,
        schema: type[BaseModel],
        model: str | None = None,
        temperature: float = 0.2,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        json_schema = schema.model_json_schema()
        return {
            "model": model or self._default_model,
            "temperature": temperature,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_context},
            ],
            "response_format": {
                "type": "json_schema",
                "json_schema": {
                    "name": schema.__name__,
                    "strict": True,
                    "schema": json_schema,
                },
            },
            "metadata": metadata or {},
        }

    def parse_and_validate(self, content: str, schema: type[BaseModel]) -> BaseModel:
        adapter: TypeAdapter[BaseModel] = TypeAdapter(schema)
        return adapter.validate_json(content)

    def generate_structured(
        self,
        *,
        system_prompt: str,
        user_context: str,
        schema: type[BaseModel],
        model: str | None = None,
        temperature: float = 0.2,
        metadata: dict[str, Any] | None = None,
    ) -> BaseModel:
        self.build_payload(
            system_prompt=system_prompt,
            user_context=user_context,
            schema=schema,
            model=model,
            temperature=temperature,
            metadata=metadata,
        )
        raise ProviderNotImplementedError("OpenRouterLLMProvider")
