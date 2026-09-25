from typing import Any

from pydantic import BaseModel

from app.schemas.competition import CompetitionAnalysis
from app.schemas.finance import FinancialAnalysis, FinancialCalculationResult
from app.schemas.geography import GeographicAnalysis
from app.schemas.market import MarketAnalysis
from app.schemas.opportunity import OpportunityAnalysis
from app.schemas.swot import SWOTAnalysis


class MockLLMProvider:
    """Test double. Does not require OPENROUTER_API_KEY."""

    def __init__(self, responses: dict[str, BaseModel] | None = None) -> None:
        self.responses = responses or {}
        self.calls: list[str] = []

    def generate_structured(
        self,
        *,
        system_prompt: str,
        user_context: str,
        schema: type[BaseModel],
        model: str | None = None,
        temperature: float = 0.2,
        metadata: dict[str, Any] | None = None,
    ) -> BaseModel:
        self.calls.append(schema.__name__)
        if schema.__name__ in self.responses:
            return self.responses[schema.__name__]
        return _empty(schema)


def _empty(schema: type[BaseModel]) -> BaseModel:
    if schema is MarketAnalysis:
        return MarketAnalysis(business="unknown", location="unknown")
    if schema is GeographicAnalysis:
        return GeographicAnalysis(location="unknown")
    if schema is CompetitionAnalysis:
        return CompetitionAnalysis()
    if schema is OpportunityAnalysis:
        return OpportunityAnalysis()
    if schema is SWOTAnalysis:
        return SWOTAnalysis()
    if schema is FinancialAnalysis:
        calc = FinancialCalculationResult(principal=0, emi=0, total_interest=0, total_repayment=0)
        return FinancialAnalysis(
            project_cost=0,
            own_investment=0,
            required_loan=0,
            calculated_values=calc,
        )
    raise TypeError(f"No mock default for {schema}")
