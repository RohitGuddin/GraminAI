from app.agents.competition.context import COMPETITION_SYSTEM_PROMPT, build_competition_context
from app.providers.interfaces.competition import CompetitionDataProvider
from app.providers.interfaces.llm import LLMProvider
from app.schemas.competition import CompetitionAnalysis
from app.schemas.workflow import WorkflowState


class CompetitionAgent:
    name = "competition"

    def __init__(
        self, competition_provider: CompetitionDataProvider, llm_provider: LLMProvider
    ) -> None:
        self._competition_provider = competition_provider
        self._llm_provider = llm_provider

    def run(self, state: WorkflowState) -> WorkflowState:
        data = self._competition_provider.search_competitors(state.request)
        analysis = self._llm_provider.generate_structured(
            system_prompt=COMPETITION_SYSTEM_PROMPT,
            user_context=build_competition_context(state.request, data),
            schema=CompetitionAnalysis,
        )
        if not isinstance(analysis, CompetitionAnalysis):
            analysis = CompetitionAnalysis.model_validate(analysis.model_dump())
        analysis.competitors = data.competitors
        state.competition_data = data
        state.competition_analysis = analysis
        return state
