from app.core.exceptions import ProviderNotImplementedError
from app.schemas.finance import GovernmentScheme


class PostgresGovernmentSchemeRepository:
    """Planned SQLAlchemy repository. Not connected in this phase."""

    def find_relevant(
        self,
        *,
        business: str,
        location: str,
        loan_required: float,
        project_cost: float,
    ) -> list[GovernmentScheme]:
        raise ProviderNotImplementedError("PostgresGovernmentSchemeRepository")

    def get_by_id(self, scheme_id: str) -> GovernmentScheme | None:
        raise ProviderNotImplementedError("PostgresGovernmentSchemeRepository")

    def search(self, query: str) -> list[GovernmentScheme]:
        raise ProviderNotImplementedError("PostgresGovernmentSchemeRepository")
