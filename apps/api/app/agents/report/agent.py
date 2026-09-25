from app.agents.report.aggregate import aggregate_final_report, lock_authoritative_finance
from app.providers.interfaces.llm import LLMProvider
from app.schemas.report import FinalReport
from app.schemas.workflow import WorkflowState
from app.workflows.barriers import assert_can_run_final_report


class FinalReportAgent:
    """Option B: optional narrative via LLM. Numbers are locked after generation."""

    name = "final_report"

    def __init__(self, llm_provider: LLMProvider | None = None) -> None:
        self._llm_provider = llm_provider

    def run(self, state: WorkflowState) -> WorkflowState:
        assert_can_run_final_report(state)
        report = aggregate_final_report(state)
        report = lock_authoritative_finance(report, state.financial_analysis)
        state.final_report = report
        return state
