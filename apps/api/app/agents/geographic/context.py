from app.schemas.geography import GeographicData
from app.schemas.request import FeasibilityRequest


def build_geographic_context(request: FeasibilityRequest, data: GeographicData) -> str:
    return (
        "User context:\n"
        f"{request.model_dump_json(indent=2)}\n\n"
        "API facts from Google Geocoding, Places (New), and Routes. "
        "Do not invent coordinates or distances. Interpret suitability separately from facts.\n"
        f"{data.model_dump_json(indent=2)}\n"
    )


GEOGRAPHIC_SYSTEM_PROMPT = (
    "You are the GraminAI Geographic Agent. Coordinates and distances are API facts. "
    "Suitability, accessibility, and constraints are interpretation."
)
