from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)



def test_admin_requires_token():

    response = client.get(
        "/api/v1/admin/dashboard"
    )


    assert response.status_code == 422