from app.core.exceptions import ProviderNotImplementedError
from app.schemas.competition import CompetitionData, Competitor
from app.schemas.request import FeasibilityRequest


class GooglePlacesCompetitionProvider:
    """Planned adapter: Google Places API (New) Text Search, Nearby Search, Place Details.

    Does not provide competitor revenue, profit, market share, or exact pricing.
    """

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def search_competitors(self, request: FeasibilityRequest) -> CompetitionData:
        raise ProviderNotImplementedError("GooglePlacesCompetitionProvider.search_competitors")

    def get_competitor_details(self, place_id: str) -> Competitor:
        raise ProviderNotImplementedError("GooglePlacesCompetitionProvider.get_competitor_details")
