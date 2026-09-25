from datetime import datetime, timezone

from app.agents.report.aggregate import aggregate_final_report, lock_authoritative_finance
from app.schemas.finance import FinancialAnalysis, FinancialCalculationResult, GovernmentScheme
from app.schemas.request import FeasibilityRequest
from app.schemas.workflow import WorkflowState


def test_final_report_does_not_change_emi_or_scheme_facts() -> None:
    request = FeasibilityRequest(
        business="dairy farm",
        location="Mysuru",
        budget=500000,
        own_investment=150000,
        loan_required=350000,
        language="kn",
    )
    calc = FinancialCalculationResult(principal=350000, emi=12345.67, total_interest=1, total_repayment=2)
    scheme = GovernmentScheme(
        scheme_name="Official Scheme",
        eligibility="must not change",
        loan_limits="10 lakh",
        subsidy="none",
        source="official Ministry source",
        last_updated=datetime.now(timezone.utc),
    )
    financial = FinancialAnalysis(
        project_cost=500000,
        own_investment=150000,
        required_loan=350000,
        calculated_values=calc,
        relevant_schemes=[scheme],
    )
    state = WorkflowState(request=request, financial_analysis=financial)
    report = aggregate_final_report(state)
    mutated = report.model_copy(
        update={
            "financial_analysis": financial.model_copy(
                update={
                    "calculated_values": calc.model_copy(update={"emi": 0.01}),
                    "relevant_schemes": [
                        scheme.model_copy(update={"eligibility": "llm invented", "loan_limits": "changed"})
                    ],
                }
            )
        }
    )
    locked = lock_authoritative_finance(mutated, financial)
    assert locked.financial_analysis is not None
    assert locked.financial_analysis.calculated_values.emi == 12345.67
    assert locked.financial_analysis.relevant_schemes[0].eligibility == "must not change"
    assert locked.financial_analysis.relevant_schemes[0].loan_limits == "10 lakh"
