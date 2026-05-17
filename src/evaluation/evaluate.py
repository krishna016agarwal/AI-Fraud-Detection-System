from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score

def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    probabilities = model.predict_proba(X_test)[:, 1]

    print("\nClassification Report:\n")

    print(
        classification_report(
            y_test,
            predictions
        )
    )

    roc_auc = roc_auc_score(
        y_test,
        probabilities
    )

    print(f"ROC-AUC Score: {roc_auc:.4f}")