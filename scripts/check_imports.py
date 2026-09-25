#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "apps" / "api"
sys.path.insert(0, str(ROOT))


def main() -> int:
    from app.agents import MarketAgent, GeographicAgent, CompetitionAgent, FinancialAgent
    from app.main import app
    from app.providers.implementations.openrouter_llm import OPENROUTER_CHAT_COMPLETIONS_URL

    assert app.title == "GraminAI API"
    assert MarketAgent.name == "market"
    assert GeographicAgent.name == "geographic"
    assert CompetitionAgent.name == "competition"
    assert FinancialAgent.name == "financial"
    assert "openrouter.ai" in OPENROUTER_CHAT_COMPLETIONS_URL
    print("imports ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
