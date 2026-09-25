from typing import Protocol

from app.schemas.competition import CompetitionData, Competitor
from app.schemas.request import FeasibilityRequest


class CompetitionDataProvider(Protocol):
    """Google Places API (New) competitor discovery. No revenue or market share."""

    def search_competitors(self, request: FeasibilityRequest) -> CompetitionData: ...

    def get_competitor_details(self, place_id: str) -> Competitor: ...
