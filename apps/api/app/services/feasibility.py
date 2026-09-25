from app.api.dependencies.providers import build_workflow, mock_providers
from app.schemas.report import FinalReport
from app.schemas.request import FeasibilityRequest
from app.schemas.workflow import WorkflowState


class FeasibilityService:
    def __init__(self, workflow=None) -> None:
        self._workflow = workflow or build_workflow(mock_providers())

    def analyze(self, request: FeasibilityRequest) -> FinalReport:
        state = WorkflowState(request=request)
        result = self._workflow.run(state)
        if result.final_report is None:
            raise RuntimeError("Workflow completed without a final report")
        return result.final_report
