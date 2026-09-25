from app.schemas.competition import CompetitionData
from app.schemas.request import FeasibilityRequest


def build_search_query(request: FeasibilityRequest) -> str:
    return f"{request.business} near {request.location}"


def build_competition_context(request: FeasibilityRequest, data: CompetitionData) -> str:
    return (
        "User context:\n"
        f"{request.model_dump_json(indent=2)}\n\n"
        "Observed Google Places (New) competitors. No revenue, profit, market share, or exact pricing "
        "unless present in this payload. Label inference separately.\n"
        f"{data.model_dump_json(indent=2)}\n"
    )


COMPETITION_SYSTEM_PROMPT = (
    "You are the GraminAI Competition Agent. Use Places data as observed. "
    "Do not fabricate financial metrics Google does not provide."
)
