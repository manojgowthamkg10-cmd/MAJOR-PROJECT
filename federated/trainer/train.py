from trainer.model_builder import build_model
from trainer.data_loader import DataLoader


class LocalTrainer:
    """
    Handles local training for a hospital.
    """

    def __init__(
        self,
        dataset_path: str,
        client_id: int,
    ):

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


    def train(self, epochs=5):

        history = self.model.fit(
            self.X_train,
            self.y_train,
            epochs=epochs,
            batch_size=32,
            verbose=0,
        )

        return history


    def get_model(self):

        return self.model