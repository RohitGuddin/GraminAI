from pydantic import BaseModel, Field

from app.schemas.common import InferredStatement, ObservedFact, SourceMetadata


class NearbyPlace(BaseModel):
    place_id: str | None = None
    name: str | None = None
    types: list[str] = Field(default_factory=list)
    latitude: float | None = None
    longitude: float | None = None
    formatted_address: str | None = None


class RouteDatum(BaseModel):
    origin: str | None = None
    destination: str | None = None
    distance_meters: float | None = None
    duration_seconds: float | None = None


class GeographicData(BaseModel):
    """Facts from Google Geocoding, Places (New), and Routes. Coordinates are never LLM-invented."""

    normalized_location: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    place_id: str | None = None
    nearby_places: list[NearbyPlace] = Field(default_factory=list)
    distance_data: list[RouteDatum] = Field(default_factory=list)
    route_data: list[RouteDatum] = Field(default_factory=list)
    source_metadata: list[SourceMetadata] = Field(default_factory=list)


class GeographicAnalysis(BaseModel):
    location: str
    location_suitability: list[InferredStatement] = Field(default_factory=list)
    accessibility: list[InferredStatement] = Field(default_factory=list)
    customer_proximity: list[InferredStatement] = Field(default_factory=list)
    supplier_access: list[InferredStatement] = Field(default_factory=list)
    constraints: list[InferredStatement] = Field(default_factory=list)
    supporting_data: list[ObservedFact] = Field(default_factory=list)
    source_metadata: list[SourceMetadata] = Field(default_factory=list)
    geographic_data: GeographicData | None = None
