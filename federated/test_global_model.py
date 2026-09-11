import numpy as np
import tensorflow as tf

from federated.utils.config import DIABETES_MODEL


def main():

    print("=" * 60)
    print("Federated Global Model Test")
    print("=" * 60)


    # Load federated global model

    model = tf.keras.models.load_model(
        DIABETES_MODEL
    )

    print("\nModel Loaded Successfully")


    # Sample patient data
    # 8 features
    # Must match diabetes.csv column order

    sample = np.array([
        [
            2,      # feature 1
            120,    # feature 2
            70,     # feature 3
            20,     # feature 4
            80,     # feature 5
            25.5,   # feature 6
            0.35,   # feature 7
            40      # feature 8
        ]
    ])


    prediction = model.predict(sample)


    probability = float(prediction[0][0])


    print("\nPrediction Probability:")
    print(probability)


    if probability >= 0.5:
        print("\nRisk Level: HIGH")
    else:
        print("\nRisk Level: LOW")


    print("=" * 60)


if __name__ == "__main__":
    main()