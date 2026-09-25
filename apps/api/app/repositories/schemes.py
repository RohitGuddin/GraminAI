from typing import Protocol

from app.schemas.finance import GovernmentScheme


class GovernmentSchemeRepository(Protocol):
    def find_relevant(
        self,
        *,
        business: str,
        location: str,
        loan_required: float,
        project_cost: float,
    ) -> list[GovernmentScheme]: ...

    def get_by_id(self, scheme_id: str) -> GovernmentScheme | None: ...

    def search(self, query: str) -> list[GovernmentScheme]: ...
