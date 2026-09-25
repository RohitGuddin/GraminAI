from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "app"


def _read(rel: str) -> str:
    return (ROOT / rel).read_text()


def test_agents_do_not_import_http_or_sql() -> None:
    forbidden = ("httpx", "requests", "sqlalchemy", "psycopg", "google.maps", "openai")
    for rel in (
        "agents/market/agent.py",
        "agents/geographic/agent.py",
        "agents/competition/agent.py",
        "agents/financial/agent.py",
        "agents/opportunity/agent.py",
        "agents/swot/agent.py",
    ):
        text = _read(rel)
        for token in forbidden:
            assert token not in text, f"{rel} contains {token}"
    assert "fetch_market_data" in _read("agents/market/agent.py")
    assert "find_relevant_schemes" in _read("agents/financial/agent.py")
    assert "search_competitors" in _read("agents/competition/agent.py")
    assert "fetch_geographic_data" in _read("agents/geographic/agent.py")
