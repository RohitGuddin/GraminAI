from app.agents.geographic.context import GEOGRAPHIC_SYSTEM_PROMPT, build_geographic_context
from app.providers.interfaces.geographic import GeographicDataProvider
from app.providers.interfaces.llm import LLMProvider
from app.schemas.geography import GeographicAnalysis
from app.schemas.workflow import WorkflowState


class GeographicAgent:
    name = "geographic"

    def __init__(
        self, geographic_provider: GeographicDataProvider, llm_provider: LLMProvider
    ) -> None:
        self._geographic_provider = geographic_provider
        self._llm_provider = llm_provider

    def run(self, state: WorkflowState) -> WorkflowState:
        data = self._geographic_provider.fetch_geographic_data(state.request)
        analysis = self._llm_provider.generate_structured(
            system_prompt=GEOGRAPHIC_SYSTEM_PROMPT,
            user_context=build_geographic_context(state.request, data),
            schema=GeographicAnalysis,
        )
        if not isinstance(analysis, GeographicAnalysis):
            analysis = GeographicAnalysis.model_validate(analysis.model_dump())
        analysis.location = state.request.location
        analysis.geographic_data = data
        state.geographic_data = data
        state.geographic_analysis = analysis
        return state
