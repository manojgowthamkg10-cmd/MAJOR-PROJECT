import flwr as fl

from federated.trainer.model_builder import build_model
from federated.trainer.data_loader import DataLoader


class BaseHospitalClient(fl.client.NumPyClient):

    def __init__(
        self,
        hospital_name: str,
        client_id: int,
        dataset_path: str,
    ):

        self.hospital_name = hospital_name
        self.client_id = client_id

        loader = DataLoader(dataset_path)

        hospitals = loader.split_for_hospitals()

        (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test,
        ) = hospitals[client_id]

        self.model = build_model(
            self.X_train.shape[1]
        )


    def get_parameters(self, config):

        return self.model.get_weights()


    def fit(self, parameters, config):

        self.model.set_weights(parameters)

        self.model.fit(
            self.X_train,
            self.y_train,
            epochs=5,
            batch_size=32,
            verbose=0,
        )

        return (
            self.model.get_weights(),
            len(self.X_train),
            {},
        )


    def evaluate(self, parameters, config):

        self.model.set_weights(parameters)

        loss, accuracy, precision, recall = (
            self.model.evaluate(
                self.X_test,
                self.y_test,
                verbose=0,
            )
        )

        return (
            float(loss),
            len(self.X_test),
            {
                "accuracy": float(accuracy),
                "precision": float(precision),
                "recall": float(recall),
            },
        )