from app.api.dependencies.providers import build_workflow, mock_providers
from app.schemas.request import FeasibilityRequest
from app.schemas.workflow import WorkflowState


def test_first_level_independent_and_opportunity_does_not_recall_providers() -> None:
    bundle = mock_providers()
    workflow = build_workflow(bundle)
    state = WorkflowState(
        request=FeasibilityRequest(
            business="dairy farm",
            location="Mysuru",
            budget=500000,
            own_investment=150000,
            loan_required=350000,
            language="kn",
        )
    )
    result = workflow.run(state)
    assert result.market_analysis is not None
    assert result.geographic_analysis is not None
    assert result.competition_analysis is not None
    assert result.financial_analysis is not None
    assert result.opportunity_analysis is not None
    assert result.swot_analysis is not None
    assert result.final_report is not None
    assert bundle.market.calls == 1
    assert bundle.geographic.calls == 1
    assert bundle.competition.calls == 1
    assert bundle.government.calls == 1
    assert "OpportunityAnalysis" in bundle.llm.calls
    assert "SWOTAnalysis" in bundle.llm.calls
