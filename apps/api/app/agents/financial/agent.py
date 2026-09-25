from datetime import datetime, timezone

from app.agents.financial.context import (
    FINANCIAL_SYSTEM_PROMPT,
    build_financial_context,
    build_financial_inputs,
)
from app.calculators.financial import FinancialCalculator
from app.providers.interfaces.government import GovernmentSchemeProvider
from app.providers.interfaces.llm import LLMProvider
from app.schemas.common import SourceMetadata
from app.schemas.finance import FinancialAnalysis
from app.schemas.workflow import WorkflowState


class FinancialAgent:
    name = "financial"

    def __init__(
        self,
        government_provider: GovernmentSchemeProvider,
        financial_calculator: FinancialCalculator,
        llm_provider: LLMProvider,
    ) -> None:
        self._government_provider = government_provider
        self._calculator = financial_calculator
        self._llm_provider = llm_provider

    def run(self, state: WorkflowState) -> WorkflowState:
        inputs = state.financial_inputs or build_financial_inputs(state.request)
        calc = self._calculator.calculate(inputs)
        schemes = self._government_provider.find_relevant_schemes(state.request)
        llm_result = self._llm_provider.generate_structured(
            system_prompt=FINANCIAL_SYSTEM_PROMPT,
            user_context=build_financial_context(state.request, calc, schemes),
            schema=FinancialAnalysis,
        )
        if not isinstance(llm_result, FinancialAnalysis):
            llm_result = FinancialAnalysis.model_validate(llm_result.model_dump())
        analysis = llm_result.model_copy(
            update={
                "project_cost": inputs.project_cost,
                "own_investment": inputs.own_investment,
                "required_loan": inputs.loan_amount,
                "calculated_values": calc,
                "relevant_schemes": schemes,
                "source_metadata": [
                    SourceMetadata(
                        source="FinancialCalculator",
                        source_type="calculated",
                        provider="python",
                        retrieved_at=datetime.now(timezone.utc),
                    )
                ],
            }
        )
        state.financial_inputs = inputs
        state.financial_calculation = calc
        state.government_schemes = schemes
        state.financial_analysis = analysis
        return state
