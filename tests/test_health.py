from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)



def test_root():

    response = client.get("/")

    assert response.status_code == 200



def test_status():

    response = client.get(
        "/api/v1/status"
    )

    assert response.status_code == 200