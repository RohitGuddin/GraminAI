from app.schemas.competition import CompetitionData, Competitor
from app.schemas.request import FeasibilityRequest


class MockCompetitionDataProvider:
    def __init__(self, data: CompetitionData | None = None) -> None:
        self.data = data or CompetitionData()
        self.calls = 0

    def search_competitors(self, request: FeasibilityRequest) -> CompetitionData:
        self.calls += 1
        return self.data

    def get_competitor_details(self, place_id: str) -> Competitor:
        return Competitor(place_id=place_id, source="mock")
