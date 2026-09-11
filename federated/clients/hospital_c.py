import flwr as fl

from federated.clients.base_client import BaseHospitalClient
from federated.utils.config import (
    SERVER_ADDRESS,
    DIABETES_DATASET,
)


if __name__ == "__main__":

    client = BaseHospitalClient(
        hospital_name="Hospital C",
        client_id=2,
        dataset_path=DIABETES_DATASET,
    )

    fl.client.start_numpy_client(
        server_address=SERVER_ADDRESS,
        client=client,
    )