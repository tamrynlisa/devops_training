import json
import pytest

from fastapi.testclient import TestClient

from src.app import app
from src.app import add_message


@pytest.fixture
def api_client() -> TestClient:
    return TestClient(app)

def test_add_message() -> None:
    test_message = "test message"

    assert add_message({}, test_message) == {"message": test_message}
    assert add_message({"response_code": 200}, test_message) == {
        "response_code": 200,
        "message": test_message
    }


def test_root_call(api_client: TestClient) -> None:
    response = api_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hi Me!"}


def test_custom_call(monkeypatch, api_client: TestClient) -> None:
    monkeypatch.setenv("MESSAGE", "hey")

    response = api_client.get("/custom")
    assert response.status_code == 200
    assert response.json() == {"message": "hey"}


def test_custom_call(api_client: TestClient) -> None:
    response = api_client.get("/version")
    assert response.status_code == 200
    assert response.json()["version"] == "0.0.0"