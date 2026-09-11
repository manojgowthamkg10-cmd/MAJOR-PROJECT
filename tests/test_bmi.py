from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)



def test_bmi():

    response = client.post(
        "/api/v1/bmi/calculate",
        json={
            "height_cm":183,
            "weight_kg":98
        }
    )


    assert response.status_code == 200

    data = response.json()

    assert "bmi" in data["data"]