from app.agents.opportunity.context import OPPORTUNITY_SYSTEM_PROMPT, build_opportunity_context
from app.providers.interfaces.llm import LLMProvider
from app.schemas.opportunity import OpportunityAnalysis
from app.schemas.workflow import WorkflowState
from app.workflows.barriers import assert_can_run_opportunity


class OpportunityAgent:
    name = "opportunity"

    def __init__(self, llm_provider: LLMProvider) -> None:
        self._llm_provider = llm_provider

    def run(self, state: WorkflowState) -> WorkflowState:
        assert_can_run_opportunity(state)
        analysis = self._llm_provider.generate_structured(
            system_prompt=OPPORTUNITY_SYSTEM_PROMPT,
            user_context=build_opportunity_context(
                state.market_analysis,
                state.geographic_analysis,
                state.competition_analysis,
                state.financial_analysis,
            ),
            schema=OpportunityAnalysis,
        )
        if not isinstance(analysis, OpportunityAnalysis):
            analysis = OpportunityAnalysis.model_validate(analysis.model_dump())
        state.opportunity_analysis = analysis
        return state
