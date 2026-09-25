from app.schemas.finance import FinancialCalculationResult, FinancialInputs, GovernmentScheme
from app.schemas.request import FeasibilityRequest


def build_financial_inputs(request: FeasibilityRequest) -> FinancialInputs:
    return FinancialInputs(
        project_cost=request.budget,
        own_investment=request.own_investment,
        loan_amount=request.loan_required,
        interest_rate=0.0,
        tenure=12,
        moratorium=0,
    )


def build_financial_context(
    request: FeasibilityRequest,
    calc: FinancialCalculationResult,
    schemes: list[GovernmentScheme],
) -> str:
    return (
        "User financial inputs:\n"
        f"{request.model_dump_json(indent=2)}\n\n"
        "Authoritative calculator results (do not change EMI, interest, repayment):\n"
        f"{calc.model_dump_json(indent=2)}\n\n"
        "Official scheme records (do not change eligibility, limits, subsidy):\n"
        f"{[s.model_dump(mode='json') for s in schemes]}\n"
        "Explain only. Do not recompute numbers or rewrite official rules."
    )


FINANCIAL_SYSTEM_PROMPT = (
    "You are the GraminAI Financial Agent. Python owns EMI and repayment. "
    "Official sources own scheme facts. You only interpret."
)
