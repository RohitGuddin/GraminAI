from app.schemas.finance import GovernmentScheme


class InMemoryGovernmentSchemeRepository:
    def __init__(self, schemes: list[GovernmentScheme] | None = None) -> None:
        self._schemes = schemes or []

    def find_relevant(
        self,
        *,
        business: str,
        location: str,
        loan_required: float,
        project_cost: float,
    ) -> list[GovernmentScheme]:
        return list(self._schemes)

    def get_by_id(self, scheme_id: str) -> GovernmentScheme | None:
        for scheme in self._schemes:
            if scheme.scheme_name == scheme_id:
                return scheme
        return None

    def search(self, query: str) -> list[GovernmentScheme]:
        needle = query.lower()
        return [s for s in self._schemes if needle in s.scheme_name.lower()]
