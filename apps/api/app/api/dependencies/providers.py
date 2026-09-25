from dataclasses import dataclass

from app.agents.competition import CompetitionAgent
from app.agents.financial import FinancialAgent
from app.agents.geographic import GeographicAgent
from app.agents.market import MarketAgent
from app.agents.opportunity import OpportunityAgent
from app.agents.report import FinalReportAgent
from app.agents.swot import SWOTAgent
from app.calculators.financial import FinancialCalculator
from app.core.config import Settings, get_settings
from app.providers.implementations.datagov_market import DataGovMarketDataProvider
from app.providers.implementations.google_maps_geographic import GoogleMapsGeographicDataProvider
from app.providers.implementations.google_places_competition import GooglePlacesCompetitionProvider
from app.providers.implementations.government_schemes import RepositoryGovernmentSchemeProvider
from app.providers.implementations.openrouter_llm import OpenRouterLLMProvider
from app.providers.interfaces.competition import CompetitionDataProvider
from app.providers.interfaces.geographic import GeographicDataProvider
from app.providers.interfaces.government import GovernmentSchemeProvider
from app.providers.interfaces.llm import LLMProvider
from app.providers.interfaces.market import MarketDataProvider
from app.providers.mocks.competition import MockCompetitionDataProvider
from app.providers.mocks.geographic import MockGeographicDataProvider
from app.providers.mocks.government import MockGovernmentSchemeProvider
from app.providers.mocks.llm import MockLLMProvider
from app.providers.mocks.market import MockMarketDataProvider
from app.repositories.memory_schemes import InMemoryGovernmentSchemeRepository
from app.workflows.graph import LangGraphWorkflow


@dataclass
class ProviderBundle:
    market: MarketDataProvider
    geographic: GeographicDataProvider
    competition: CompetitionDataProvider
    government: GovernmentSchemeProvider
    llm: LLMProvider
    calculator: FinancialCalculator


def production_providers(settings: Settings | None = None) -> ProviderBundle:
    settings = settings or get_settings()
    return ProviderBundle(
        market=DataGovMarketDataProvider(settings.data_gov_in_api_key),
        geographic=GoogleMapsGeographicDataProvider(settings.google_maps_api_key),
        competition=GooglePlacesCompetitionProvider(settings.google_maps_api_key),
        government=RepositoryGovernmentSchemeProvider(InMemoryGovernmentSchemeRepository()),
        llm=OpenRouterLLMProvider(settings.openrouter_api_key, settings.openrouter_model),
        calculator=FinancialCalculator(),
    )


def mock_providers() -> ProviderBundle:
    return ProviderBundle(
        market=MockMarketDataProvider(),
        geographic=MockGeographicDataProvider(),
        competition=MockCompetitionDataProvider(),
        government=MockGovernmentSchemeProvider(),
        llm=MockLLMProvider(),
        calculator=FinancialCalculator(),
    )


def build_workflow(bundle: ProviderBundle) -> LangGraphWorkflow:
    return LangGraphWorkflow(
        market=MarketAgent(bundle.market, bundle.llm),
        geographic=GeographicAgent(bundle.geographic, bundle.llm),
        competition=CompetitionAgent(bundle.competition, bundle.llm),
        financial=FinancialAgent(bundle.government, bundle.calculator, bundle.llm),
        opportunity=OpportunityAgent(bundle.llm),
        swot=SWOTAgent(bundle.llm),
        report=FinalReportAgent(bundle.llm),
    )
