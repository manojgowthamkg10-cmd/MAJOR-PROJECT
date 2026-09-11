from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)


class Evaluator:
    """
    Evaluates trained models.
    """

    def __init__(
        self,
        model,
        X_test,
        y_test,
    ):

        self.model = model
        self.X_test = X_test
        self.y_test = y_test


    def evaluate(self):

        predictions = (
            self.model.predict(
                self.X_test
            )
        )

        predictions = (
            predictions > 0.5
        ).astype(int)


        return {
            "accuracy": accuracy_score(
                self.y_test,
                predictions,
            ),

            "precision": precision_score(
                self.y_test,
                predictions,
                zero_division=0,
            ),

            "recall": recall_score(
                self.y_test,
                predictions,
                zero_division=0,
            ),

            "f1_score": f1_score(
                self.y_test,
                predictions,
                zero_division=0,
            ),
        }