from datetime import datetime

from pydantic import BaseModel, Field

from app.schemas.common import InferredStatement, SourceMetadata


class FinancialInputs(BaseModel):
    project_cost: float = Field(gt=0)
    own_investment: float = Field(ge=0)
    loan_amount: float = Field(ge=0)
    interest_rate: float = Field(ge=0, description="Annual percentage rate")
    tenure: int = Field(gt=0, description="Tenure in months")
    moratorium: int = Field(ge=0, description="Moratorium in months")


class RepaymentInstallment(BaseModel):
    period: int
    emi: float
    principal_component: float
    interest_component: float
    remaining_principal: float


class FinancialCalculationResult(BaseModel):
    """Authoritative Python calculator output. The LLM must not change these numbers."""

    principal: float
    emi: float
    total_interest: float
    total_repayment: float
    repayment_schedule: list[RepaymentInstallment] = Field(default_factory=list)
    calculation_method: str = "reducing_balance_emi"
    calculated_at: datetime | None = None


class GovernmentScheme(BaseModel):
    scheme_name: str
    description: str | None = None
    eligibility: str | None = None
    loan_limits: str | None = None
    subsidy: str | None = None
    interest_information: str | None = None
    required_documents: list[str] = Field(default_factory=list)
    source: str
    source_url: str | None = None
    last_updated: datetime | None = None
    source_metadata: SourceMetadata | None = None


class FinancialAnalysis(BaseModel):
    project_cost: float
    own_investment: float
    required_loan: float
    calculated_values: FinancialCalculationResult
    relevant_schemes: list[GovernmentScheme] = Field(default_factory=list)
    financial_risks: list[InferredStatement] = Field(default_factory=list)
    interpretation: list[InferredStatement] = Field(default_factory=list)
    source_metadata: list[SourceMetadata] = Field(default_factory=list)
