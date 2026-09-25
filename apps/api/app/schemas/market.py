from datetime import date as Date
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.common import InferredStatement, ObservedFact, SourceMetadata


class MarketData(BaseModel):
    """Mandi/commodity price row from data.gov.in / AGMARKNET. No demand fields."""

    model_config = ConfigDict(populate_by_name=True)

    commodity: str | None = None
    variety: str | None = None
    state: str | None = None
    district: str | None = None
    market: str | None = None
    minimum_price: float | None = None
    maximum_price: float | None = None
    modal_price: float | None = None
    price_unit: str | None = None
    price_date: Date | None = Field(default=None, alias="date")
    source: str = "data.gov.in / AGMARKNET"
    source_url: str | None = None
    retrieved_at: datetime | None = None
    source_metadata: SourceMetadata | None = None


class MarketAnalysis(BaseModel):
    """LLM analysis plus attached source rows. Demand is inference, not API data."""

    business: str
    location: str
    demand_indicators: list[InferredStatement] = Field(default_factory=list)
    target_customers: list[InferredStatement] = Field(default_factory=list)
    pricing_conditions: list[InferredStatement] = Field(default_factory=list)
    market_conditions: list[InferredStatement] = Field(default_factory=list)
    challenges: list[InferredStatement] = Field(default_factory=list)
    supporting_data: list[ObservedFact] = Field(default_factory=list)
    source_metadata: list[SourceMetadata] = Field(default_factory=list)
    market_data: list[MarketData] = Field(default_factory=list)
