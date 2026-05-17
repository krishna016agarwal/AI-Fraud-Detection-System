from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

def preprocess_data(df):

    X = df.drop("Class", axis=1)
    y = df["Class"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    smote = SMOTE(random_state=42)

    X_train_resampled, y_train_resampled = smote.fit_resample(
        X_train_scaled,
        y_train
    )

    return (
        X_train_resampled,
        X_test_scaled,
        y_train_resampled,
        y_test,
        scaler
    )