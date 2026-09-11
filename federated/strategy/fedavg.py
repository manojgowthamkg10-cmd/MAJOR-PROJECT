import flwr as fl

from federated.utils.config import DIABETES_MODEL
from federated.trainer.model_builder import build_model


class FederatedAveragingStrategy(fl.server.strategy.FedAvg):

    def __init__(self):

        super().__init__(
            fraction_fit=1.0,
            fraction_evaluate=1.0,
            min_fit_clients=3,
            min_evaluate_clients=3,
            min_available_clients=3,
            on_fit_config_fn=self.fit_config,
            on_evaluate_config_fn=self.evaluate_config,
        )

    def fit_config(self, server_round):

        return {
            "server_round": server_round,
            "local_epochs": 5,
        }

    def evaluate_config(self, server_round):

        return {
            "server_round": server_round,
        }

    def aggregate_fit(
        self,
        server_round,
        results,
        failures,
    ):

        aggregated_parameters = super().aggregate_fit(
            server_round,
            results,
            failures,
        )

        if aggregated_parameters[0] is not None:

            model = build_model(8)

            weights = fl.common.parameters_to_ndarrays(
                aggregated_parameters[0]
            )

            model.set_weights(weights)

            model.save(
                DIABETES_MODEL
            )

            print(
                f"Global model saved after round {server_round}"
            )

        return aggregated_parameters