from sklearn.ensemble import RandomForestClassifier
import joblib
import os
from src.evaluation.evaluate import evaluate_model
from src.ingestion.load_data import load_dataset
from src.preprocessing.preprocess import preprocess_data

def train():

    df = load_dataset()

    (
        X_train,
        X_test,
        y_train,
        y_test,
        scaler
    ) = preprocess_data(df)

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    os.makedirs("models", exist_ok=True)

    evaluate_model(
    model,
    X_test,
    y_test
) 
    joblib.dump(
        model,
        "models/random_forest_model.pkl"
    )

    joblib.dump(
        scaler,
        "models/scaler.pkl"
    )

    print("Model training completed")

if __name__ == "__main__":
    train()