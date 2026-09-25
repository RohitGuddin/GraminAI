import pytest

from app.schemas.competition import CompetitionAnalysis
from app.schemas.finance import FinancialAnalysis, FinancialCalculationResult
from app.schemas.geography import GeographicAnalysis
from app.schemas.market import MarketAnalysis
from app.schemas.opportunity import OpportunityAnalysis
from app.schemas.request import FeasibilityRequest
from app.schemas.swot import SWOTAnalysis
from app.schemas.workflow import WorkflowState
from app.workflows.barriers import (
    WorkflowBarrierError,
    can_run_opportunity,
    can_run_swot,
    assert_can_run_opportunity,
    assert_can_run_swot,
)


def _request() -> FeasibilityRequest:
    return FeasibilityRequest(
        business="dairy farm",
        location="Mysuru",
        budget=500000,
        own_investment=150000,
        loan_required=350000,
        language="kn",
    )


def _calc() -> FinancialCalculationResult:
    return FinancialCalculationResult(principal=1, emi=1, total_interest=0, total_repayment=1)


def test_opportunity_waits_for_four() -> None:
    state = WorkflowState(request=_request())
    assert can_run_opportunity(state) is False
    with pytest.raises(WorkflowBarrierError):
        assert_can_run_opportunity(state)
    state.market_analysis = MarketAnalysis(business="x", location="y")
    state.geographic_analysis = GeographicAnalysis(location="y")
    state.competition_analysis = CompetitionAnalysis()
    state.financial_analysis = FinancialAnalysis(
        project_cost=1, own_investment=1, required_loan=1, calculated_values=_calc()
    )
    assert can_run_opportunity(state) is True


def test_swot_waits_for_five() -> None:
    state = WorkflowState(request=_request())
    state.market_analysis = MarketAnalysis(business="x", location="y")
    state.geographic_analysis = GeographicAnalysis(location="y")
    state.competition_analysis = CompetitionAnalysis()
    state.financial_analysis = FinancialAnalysis(
        project_cost=1, own_investment=1, required_loan=1, calculated_values=_calc()
    )
    assert can_run_swot(state) is False
    with pytest.raises(WorkflowBarrierError):
        assert_can_run_swot(state)
    state.opportunity_analysis = OpportunityAnalysis()
    assert can_run_swot(state) is True
    assert SWOTAnalysis().strengths == []
