from app.schemas.competition import CompetitionAnalysis
from app.schemas.finance import FinancialAnalysis
from app.schemas.geography import GeographicAnalysis
from app.schemas.market import MarketAnalysis


def build_opportunity_context(
    market: MarketAnalysis,
    geographic: GeographicAnalysis,
    competition: CompetitionAnalysis,
    financial: FinancialAnalysis,
) -> str:
    return (
        "Synthesize opportunities from existing analyses. Do not call external APIs. "
        "Do not recompute EMI.\n"
        f"market={market.model_dump_json()}\n"
        f"geographic={geographic.model_dump_json()}\n"
        f"competition={competition.model_dump_json()}\n"
        f"financial={financial.model_dump_json()}\n"
    )


OPPORTUNITY_SYSTEM_PROMPT = (
    "You are the GraminAI Opportunity Agent. Use only the four upstream analyses."
)
