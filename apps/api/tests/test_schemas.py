import pytest
from pydantic import ValidationError

from app.schemas.request import FeasibilityRequest


def test_request_validation() -> None:
    payload = FeasibilityRequest(
        business="dairy farm",
        location="Mysuru",
        budget=500000,
        own_investment=150000,
        loan_required=350000,
        language="kn",
    )
    assert payload.business == "dairy farm"


def test_request_rejects_empty_business() -> None:
    with pytest.raises(ValidationError):
        FeasibilityRequest(
            business="",
            location="Mysuru",
            budget=1,
            own_investment=1,
            loan_required=0,
            language="en",
        )
