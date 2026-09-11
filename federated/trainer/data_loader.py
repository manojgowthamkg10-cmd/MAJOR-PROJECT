import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class DataLoader:

    def __init__(self, dataset_path: str):

        self.dataset_path = dataset_path

    def load_data(self):

        df = pd.read_csv(self.dataset_path)

        X = df.iloc[:, :-1].values
        y = df.iloc[:, -1].values

        return X, y

    def split_for_hospitals(self):

        X, y = self.load_data()

        indices = np.random.permutation(len(X))

        X = X[indices]
        y = y[indices]

        X_split = np.array_split(X, 3)
        y_split = np.array_split(y, 3)

        hospitals = []

        for i in range(3):

            X_train, X_test, y_train, y_test = train_test_split(
                X_split[i],
                y_split[i],
                test_size=0.2,
                random_state=42,
            )

            scaler = StandardScaler()

            X_train = scaler.fit_transform(X_train)
            X_test = scaler.transform(X_test)

            hospitals.append(
                (
                    X_train,
                    X_test,
                    y_train,
                    y_test,
                )
            )

        return hospitals