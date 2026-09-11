from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)



def test_diabetes_schema_validation():

    response = client.post(
        "/api/v1/predict/diabetes",
        json={
            "token":{
                "id_token":"test"
            },
            "request":{
                "pregnancies":2,
                "glucose":140,
                "blood_pressure":80,
                "skin_thickness":25,
                "insulin":100,
                "bmi":28.5,
                "diabetes_pedigree_function":0.5,
                "age":45
            }
        }
    )


    # Firebase token will fail,
    # but API should respond

    assert response.status_code in [
        400,
        401
    ]