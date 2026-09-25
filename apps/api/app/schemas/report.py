from pydantic import BaseModel, Field

from app.schemas.competition import CompetitionAnalysis
from app.schemas.finance import FinancialAnalysis
from app.schemas.geography import GeographicAnalysis
from app.schemas.market import MarketAnalysis
from app.schemas.opportunity import OpportunityAnalysis
from app.schemas.request import FeasibilityRequest
from app.schemas.swot import SWOTAnalysis
from app.schemas.common import InferredStatement, SourceMetadata


class FinalReport(BaseModel):
    request: FeasibilityRequest
    executive_summary: list[InferredStatement] = Field(default_factory=list)
    market_analysis: MarketAnalysis | None = None
    geographic_analysis: GeographicAnalysis | None = None
    competition_analysis: CompetitionAnalysis | None = None
    financial_analysis: FinancialAnalysis | None = None
    opportunity_analysis: OpportunityAnalysis | None = None
    swot_analysis: SWOTAnalysis | None = None
    recommendations: list[InferredStatement] = Field(default_factory=list)
    sources: list[SourceMetadata] = Field(default_factory=list)
    metadata: dict[str, str] = Field(default_factory=dict)
