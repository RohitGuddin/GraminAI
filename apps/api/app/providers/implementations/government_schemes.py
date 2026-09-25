from app.repositories.schemes import GovernmentSchemeRepository
from app.schemas.finance import GovernmentScheme
from app.schemas.request import FeasibilityRequest


class RepositoryGovernmentSchemeProvider:
    """Reads schemes via repository only. FinancialAgent never opens PostgreSQL."""

    def __init__(self, repository: GovernmentSchemeRepository) -> None:
        self._repository = repository

    def find_relevant_schemes(self, request: FeasibilityRequest) -> list[GovernmentScheme]:
        return self._repository.find_relevant(
            business=request.business,
            location=request.location,
            loan_required=request.loan_required,
            project_cost=request.budget,
        )

    def get_scheme(self, scheme_id: str) -> GovernmentScheme | None:
        return self._repository.get_by_id(scheme_id)

    def search_schemes(self, query: str) -> list[GovernmentScheme]:
        return self._repository.search(query)
