from typing import Protocol

from app.schemas.finance import GovernmentScheme
from app.schemas.request import FeasibilityRequest


class GovernmentSchemeProvider(Protocol):
    """Reads normalized schemes. Does not talk to a fictional Government Loan API."""

    def find_relevant_schemes(self, request: FeasibilityRequest) -> list[GovernmentScheme]: ...

    def get_scheme(self, scheme_id: str) -> GovernmentScheme | None: ...

    def search_schemes(self, query: str) -> list[GovernmentScheme]: ...
