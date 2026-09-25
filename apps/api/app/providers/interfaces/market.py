from typing import Protocol

from app.schemas.market import MarketData
from app.schemas.request import FeasibilityRequest


class MarketDataProvider(Protocol):
    """Retrieves AGMARKNET-style mandi prices. Does not provide demand."""

    def fetch_market_data(self, request: FeasibilityRequest) -> list[MarketData]: ...
