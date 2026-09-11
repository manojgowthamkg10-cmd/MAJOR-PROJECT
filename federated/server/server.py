import flwr as fl

from federated.strategy.fedavg import FederatedAveragingStrategy
from federated.utils.config import (
    SERVER_ADDRESS,
    NUM_ROUNDS,
)


def main():

    print("=" * 60)
    print("Federated Learning Server Started")
    print("=" * 60)

    strategy = FederatedAveragingStrategy()

    fl.server.start_server(
        server_address=SERVER_ADDRESS,
        config=fl.server.ServerConfig(
            num_rounds=NUM_ROUNDS,
        ),
        strategy=strategy,
    )


if __name__ == "__main__":
    main()