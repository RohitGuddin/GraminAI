"""LangGraph-shaped orchestrator: four parallel nodes, then opportunity, SWOT, report."""

import asyncio

from app.agents.competition import CompetitionAgent
from app.agents.financial import FinancialAgent
from app.agents.geographic import GeographicAgent
from app.agents.market import MarketAgent
from app.agents.opportunity import OpportunityAgent
from app.agents.report import FinalReportAgent
from app.agents.swot import SWOTAgent
from app.schemas.workflow import WorkflowState


class LangGraphWorkflow:
    FIRST_LEVEL = ("market", "geographic", "competition", "financial")

    def __init__(
        self,
        market: MarketAgent,
        geographic: GeographicAgent,
        competition: CompetitionAgent,
        financial: FinancialAgent,
        opportunity: OpportunityAgent,
        swot: SWOTAgent,
        report: FinalReportAgent,
    ) -> None:
        self._market = market
        self._geographic = geographic
        self._competition = competition
        self._financial = financial
        self._opportunity = opportunity
        self._swot = swot
        self._report = report

    def run(self, state: WorkflowState) -> WorkflowState:
        return asyncio.run(self.run_async(state))

    async def run_async(self, state: WorkflowState) -> WorkflowState:
        copies = [state.model_copy(deep=True) for _ in range(4)]
        market_s, geo_s, comp_s, fin_s = await asyncio.gather(
            asyncio.to_thread(self._market.run, copies[0]),
            asyncio.to_thread(self._geographic.run, copies[1]),
            asyncio.to_thread(self._competition.run, copies[2]),
            asyncio.to_thread(self._financial.run, copies[3]),
        )
        merged = state.model_copy(deep=True)
        merged.market_data = market_s.market_data
        merged.market_analysis = market_s.market_analysis
        merged.errors.market_error = market_s.errors.market_error
        merged.geographic_data = geo_s.geographic_data
        merged.geographic_analysis = geo_s.geographic_analysis
        merged.errors.geographic_error = geo_s.errors.geographic_error
        merged.competition_data = comp_s.competition_data
        merged.competition_analysis = comp_s.competition_analysis
        merged.errors.competition_error = comp_s.errors.competition_error
        merged.financial_inputs = fin_s.financial_inputs
        merged.financial_calculation = fin_s.financial_calculation
        merged.government_schemes = fin_s.government_schemes
        merged.financial_analysis = fin_s.financial_analysis
        merged.errors.financial_error = fin_s.errors.financial_error

        merged = self._opportunity.run(merged)
        merged = self._swot.run(merged)
        return self._report.run(merged)
