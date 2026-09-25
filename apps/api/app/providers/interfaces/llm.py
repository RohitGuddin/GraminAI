from typing import Any, Protocol, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class LLMProvider(Protocol):
    """Agents depend on this interface, never on OpenRouter HTTP directly."""

    def generate_structured(
        self,
        *,
        system_prompt: str,
        user_context: str,
        schema: type[T],
        model: str | None = None,
        temperature: float = 0.2,
        metadata: dict[str, Any] | None = None,
    ) -> T: ...
