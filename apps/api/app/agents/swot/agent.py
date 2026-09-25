from app.agents.swot.context import SWOT_SYSTEM_PROMPT, build_swot_context
from app.providers.interfaces.llm import LLMProvider
from app.schemas.swot import SWOTAnalysis
from app.schemas.workflow import WorkflowState
from app.workflows.barriers import assert_can_run_swot


class SWOTAgent:
    name = "swot"

    def __init__(self, llm_provider: LLMProvider) -> None:
        self._llm_provider = llm_provider

    def run(self, state: WorkflowState) -> WorkflowState:
        assert_can_run_swot(state)
        analysis = self._llm_provider.generate_structured(
            system_prompt=SWOT_SYSTEM_PROMPT,
            user_context=build_swot_context(
                state.market_analysis,
                state.geographic_analysis,
                state.competition_analysis,
                state.financial_analysis,
                state.opportunity_analysis,
            ),
            schema=SWOTAnalysis,
        )
        if not isinstance(analysis, SWOTAnalysis):
            analysis = SWOTAnalysis.model_validate(analysis.model_dump())
        state.swot_analysis = analysis
        return state
