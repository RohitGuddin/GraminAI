from pydantic import BaseModel, Field

from app.schemas.competition import CompetitionAnalysis, CompetitionData
from app.schemas.finance import (
    FinancialAnalysis,
    FinancialCalculationResult,
    FinancialInputs,
    GovernmentScheme,
)
from app.schemas.geography import GeographicAnalysis, GeographicData
from app.schemas.market import MarketAnalysis, MarketData
from app.schemas.opportunity import OpportunityAnalysis
from app.schemas.report import FinalReport
from app.schemas.request import FeasibilityRequest
from app.schemas.swot import SWOTAnalysis


class WorkflowErrors(BaseModel):
    market_error: str | None = None
    geographic_error: str | None = None
    competition_error: str | None = None
    financial_error: str | None = None
    opportunity_error: str | None = None
    swot_error: str | None = None
    report_error: str | None = None


class WorkflowMetadata(BaseModel):
    request_id: str | None = None
    language: str | None = None
    extra: dict[str, str] = Field(default_factory=dict)


class WorkflowState(BaseModel):
    """LangGraph state. First-level agents write only their own keys."""

    request: FeasibilityRequest

    market_data: list[MarketData] = Field(default_factory=list)
    market_analysis: MarketAnalysis | None = None

    geographic_data: GeographicData | None = None
    geographic_analysis: GeographicAnalysis | None = None

    competition_data: CompetitionData | None = None
    competition_analysis: CompetitionAnalysis | None = None

    financial_inputs: FinancialInputs | None = None
    financial_calculation: FinancialCalculationResult | None = None
    government_schemes: list[GovernmentScheme] = Field(default_factory=list)
    financial_analysis: FinancialAnalysis | None = None

    opportunity_analysis: OpportunityAnalysis | None = None
    swot_analysis: SWOTAnalysis | None = None
    final_report: FinalReport | None = None

    errors: WorkflowErrors = Field(default_factory=WorkflowErrors)
    metadata: WorkflowMetadata = Field(default_factory=WorkflowMetadata)
