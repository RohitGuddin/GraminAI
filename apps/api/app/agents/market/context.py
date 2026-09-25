from app.schemas.market import MarketData
from app.schemas.request import FeasibilityRequest


def build_market_context(request: FeasibilityRequest, rows: list[MarketData]) -> str:
    payload = [row.model_dump(mode="json") for row in rows]
    return (
        "User business context (not API data):\n"
        f"{request.model_dump_json(indent=2)}\n\n"
        "Observed AGMARKNET/data.gov.in price rows. Do not invent missing statistics. "
        "Demand indicators are inference only. Mention data freshness and limitations.\n"
        f"{payload}\n"
    )


MARKET_SYSTEM_PROMPT = (
    "You are the GraminAI Market Agent. Use provided mandi price data only as observed facts. "
    "Do not invent demand, customer preferences, or missing prices. Distinguish observed vs inference."
)
