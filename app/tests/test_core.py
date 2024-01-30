import sys

sys.path.append(".")
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/health")
    assert response.status_code == 200
