from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_feasibility_route_uses_service_not_agents() -> None:
    response = client.post(
        "/api/v1/feasibility",
        json={
            "business": "dairy farm",
            "location": "Mysuru",
            "budget": 500000,
            "own_investment": 150000,
            "loan_required": 350000,
            "language": "kn",
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert body["request"]["location"] == "Mysuru"
    assert body["financial_analysis"]["calculated_values"]["emi"] is not None
