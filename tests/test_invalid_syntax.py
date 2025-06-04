import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.parametrize("dsl", [
    "age >> 65",             # invalid operator
    "status in [active,p]",  # missing quotes
    "not (age > 70",         # unclosed paren
])
def test_syntax_error_returns_400(dsl):
    resp = client.post("/evaluate_rules/", json={
        "context": "any",
        "facts": {"age": 75, "status": "active"}
    ,   "conditions": dsl
    })
    assert resp.status_code == 400
    assert "Syntax error" in resp.json()["detail"]
