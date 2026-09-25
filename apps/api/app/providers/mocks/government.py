from app.schemas.finance import GovernmentScheme
from app.schemas.request import FeasibilityRequest


class MockGovernmentSchemeProvider:
    def __init__(self, schemes: list[GovernmentScheme] | None = None) -> None:
        self.schemes = schemes or []
        self.calls = 0

    def find_relevant_schemes(self, request: FeasibilityRequest) -> list[GovernmentScheme]:
        self.calls += 1
        return list(self.schemes)

    def get_scheme(self, scheme_id: str) -> GovernmentScheme | None:
        for scheme in self.schemes:
            if scheme.scheme_name == scheme_id:
                return scheme
        return None

    def search_schemes(self, query: str) -> list[GovernmentScheme]:
        return [s for s in self.schemes if query.lower() in s.scheme_name.lower()]
