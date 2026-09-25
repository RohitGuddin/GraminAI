from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class SourceMetadata(BaseModel):
    """Provenance for external or calculated data. Not LLM inference."""

    source: str
    source_type: str | None = None
    source_url: str | None = None
    retrieved_at: datetime | None = None
    provider: str | None = None
    data_freshness: str | None = None
    last_updated: datetime | None = None


class ObservedFact(BaseModel):
    """A value that came from an API or calculator."""

    label: str
    value: str
    provenance: SourceMetadata
    kind: Literal["source", "calculated"] = "source"


class InferredStatement(BaseModel):
    """LLM-derived analysis. Must not be treated as API data."""

    statement: str
    based_on: list[str] = Field(default_factory=list)
    kind: Literal["llm"] = "llm"
