from app.schemas.finance import FinancialAnalysis, GovernmentScheme
from app.schemas.report import FinalReport
from app.schemas.workflow import WorkflowState


def aggregate_final_report(state: WorkflowState) -> FinalReport:
    """Option A: copy structured values. Preserves calculator and scheme fields."""
    sources = []
    if state.market_analysis:
        sources.extend(state.market_analysis.source_metadata)
    if state.geographic_analysis:
        sources.extend(state.geographic_analysis.source_metadata)
    if state.competition_analysis:
        sources.extend(state.competition_analysis.source_metadata)
    if state.financial_analysis:
        sources.extend(state.financial_analysis.source_metadata)
    return FinalReport(
        request=state.request,
        market_analysis=state.market_analysis,
        geographic_analysis=state.geographic_analysis,
        competition_analysis=state.competition_analysis,
        financial_analysis=state.financial_analysis,
        opportunity_analysis=state.opportunity_analysis,
        swot_analysis=state.swot_analysis,
        sources=sources,
        metadata={"generator": "python_aggregation"},
    )


def lock_authoritative_finance(
    report: FinalReport, financial: FinancialAnalysis | None
) -> FinalReport:
    """Reject LLM overwrites of EMI and official scheme facts."""
    if financial is None or report.financial_analysis is None:
        return report
    locked = report.financial_analysis.model_copy(
        update={
            "calculated_values": financial.calculated_values,
            "relevant_schemes": [
                GovernmentScheme.model_validate(s.model_dump()) for s in financial.relevant_schemes
            ],
            "project_cost": financial.project_cost,
            "own_investment": financial.own_investment,
            "required_loan": financial.required_loan,
        }
    )
    return report.model_copy(update={"financial_analysis": locked})
