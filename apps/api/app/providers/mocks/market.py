from app.schemas.market import MarketData
from app.schemas.request import FeasibilityRequest


class MockMarketDataProvider:
    def __init__(self, rows: list[MarketData] | None = None) -> None:
        self.rows = rows or []
        self.calls = 0

    def fetch_market_data(self, request: FeasibilityRequest) -> list[MarketData]:
        self.calls += 1
        return list(self.rows)
