from app.providers.interfaces.llm import LLMProvider
from app.providers.interfaces.market import MarketDataProvider
from app.schemas.market import MarketAnalysis
from app.schemas.request import FeasibilityRequest
from app.schemas.workflow import WorkflowState
from app.agents.market.context import MARKET_SYSTEM_PROMPT, build_market_context


class MarketAgent:
    name = "market"

    def __init__(self, market_provider: MarketDataProvider, llm_provider: LLMProvider) -> None:
        self._market_provider = market_provider
        self._llm_provider = llm_provider

    def run(self, state: WorkflowState) -> WorkflowState:
        request = state.request
        rows = self._market_provider.fetch_market_data(request)
        analysis = self._llm_provider.generate_structured(
            system_prompt=MARKET_SYSTEM_PROMPT,
            user_context=build_market_context(request, rows),
            schema=MarketAnalysis,
        )
        if not isinstance(analysis, MarketAnalysis):
            analysis = MarketAnalysis.model_validate(analysis.model_dump())
        analysis.market_data = rows
        analysis.business = request.business
        analysis.location = request.location
        state.market_data = rows
        state.market_analysis = analysis
        return state
