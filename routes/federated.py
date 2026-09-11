from fastapi import APIRouter

from federated.server import start_server
from utils.response import success_response, error_response

router = APIRouter()


@router.get("/status")
def get_status():
    return success_response(
        message="Federated Learning Status",
        data={
            "status": "Ready",
            "clients": 3,
            "rounds": 5,
            "strategy": "FedAvg",
        },
    )


@router.post("/start")
def start_federated_training():
    try:
        start_server()

        return success_response(
            message="Federated Learning started successfully",
            data={
                "status": "Training Started",
            },
        )

    except Exception as e:
        return error_response(
            message=str(e),
            status_code=400,
        )


@router.get("/clients")
def get_clients():
    return success_response(
        message="Connected Clients",
        data=[
            {
                "id": "Hospital-A",
                "status": "Connected",
            },
            {
                "id": "Hospital-B",
                "status": "Connected",
            },
            {
                "id": "Hospital-C",
                "status": "Connected",
            },
        ],
    )


@router.get("/global-model")
def get_global_model():
    return success_response(
        message="Global Model",
        data={
            "model": "RandomForestClassifier",
            "aggregation": "FedAvg",
            "version": "1.0",
        },
    )