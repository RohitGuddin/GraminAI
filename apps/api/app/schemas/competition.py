from pydantic import BaseModel, Field

from app.schemas.common import InferredStatement, SourceMetadata


class Competitor(BaseModel):
    """Normalized Google Places (New) business. No revenue, profit, or market share."""

    place_id: str | None = None
    name: str | None = None
    category: str | None = None
    address: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    rating: float | None = None
    user_rating_count: int | None = None
    business_status: str | None = None
    website: str | None = None
    source: str = "Google Places API (New)"


class CompetitionData(BaseModel):
    competitors: list[Competitor] = Field(default_factory=list)
    source_metadata: list[SourceMetadata] = Field(default_factory=list)


class CompetitionAnalysis(BaseModel):
    competition_level: InferredStatement | None = None
    competitors: list[Competitor] = Field(default_factory=list)
    pricing_pressure: list[InferredStatement] = Field(default_factory=list)
    competitive_factors: list[InferredStatement] = Field(default_factory=list)
    differentiation_opportunities: list[InferredStatement] = Field(default_factory=list)
    market_gaps: list[InferredStatement] = Field(default_factory=list)
    source_metadata: list[SourceMetadata] = Field(default_factory=list)
