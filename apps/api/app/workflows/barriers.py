from app.schemas.workflow import WorkflowState


class WorkflowBarrierError(RuntimeError):
    pass


def can_run_opportunity(state: WorkflowState) -> bool:
    return all(
        [
            state.market_analysis is not None,
            state.geographic_analysis is not None,
            state.competition_analysis is not None,
            state.financial_analysis is not None,
        ]
    )


def can_run_swot(state: WorkflowState) -> bool:
    return can_run_opportunity(state) and state.opportunity_analysis is not None


def can_run_final_report(state: WorkflowState) -> bool:
    return can_run_swot(state) and state.swot_analysis is not None


def assert_can_run_opportunity(state: WorkflowState) -> None:
    if not can_run_opportunity(state):
        raise WorkflowBarrierError("Opportunity requires market, geographic, competition, and financial analyses")


def assert_can_run_swot(state: WorkflowState) -> None:
    if not can_run_swot(state):
        raise WorkflowBarrierError("SWOT requires four first-level analyses plus opportunity")


def assert_can_run_final_report(state: WorkflowState) -> None:
    if not can_run_final_report(state):
        raise WorkflowBarrierError("Final report requires SWOT")
