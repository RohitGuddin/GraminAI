from fastapi import APIRouter, Depends

from app.schemas.report import FinalReport
from app.schemas.request import FeasibilityRequest
from app.services.feasibility import FeasibilityService

router = APIRouter()


def get_feasibility_service() -> FeasibilityService:
    return FeasibilityService()


@router.post("/feasibility", response_model=FinalReport)
def create_feasibility(
    payload: FeasibilityRequest,
    service: FeasibilityService = Depends(get_feasibility_service),
) -> FinalReport:
    return service.analyze(payload)
