from app.schemas.competition import CompetitionAnalysis
from app.schemas.finance import FinancialAnalysis
from app.schemas.geography import GeographicAnalysis
from app.schemas.market import MarketAnalysis
from app.schemas.opportunity import OpportunityAnalysis


def build_swot_context(
    market: MarketAnalysis,
    geographic: GeographicAnalysis,
    competition: CompetitionAnalysis,
    financial: FinancialAnalysis,
    opportunity: OpportunityAnalysis,
) -> str:
    return (
        "Synthesize SWOT from five analyses. Do not call external APIs or the calculator.\n"
        f"market={market.model_dump_json()}\n"
        f"geographic={geographic.model_dump_json()}\n"
        f"competition={competition.model_dump_json()}\n"
        f"financial={financial.model_dump_json()}\n"
        f"opportunity={opportunity.model_dump_json()}\n"
    )


SWOT_SYSTEM_PROMPT = "You are the GraminAI SWOT Agent. Use only workflow state."
