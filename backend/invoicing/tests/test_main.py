from fastapi.testclient import TestClient
from src.jrj_invoicing.main import app

client = TestClient(app)


def test_read_index():
    """
    Test the index endpoint.

    Assert the response string & status code
    :return:
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "Up!"}
