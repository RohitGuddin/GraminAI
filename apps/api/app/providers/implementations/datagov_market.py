from app.core.exceptions import ProviderNotImplementedError
from app.schemas.market import MarketData
from app.schemas.request import FeasibilityRequest


class DataGovMarketDataProvider:
    """Planned adapter: data.gov.in resource associated with AGMARKNET mandi prices.

    Uses DATA_GOV_IN_API_KEY. Does not invent demand statistics.
    HTTP is not implemented in this architecture phase.
    """

    SOURCE = "data.gov.in / AGMARKNET"

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def fetch_market_data(self, request: FeasibilityRequest) -> list[MarketData]:
        raise ProviderNotImplementedError("DataGovMarketDataProvider")
