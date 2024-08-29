import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def train_model():
    # Load the dataset
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

    # Start an MLflow run
    with mlflow.start_run():
        # Train a model
        clf = RandomForestClassifier(n_estimators=100)
        clf.fit(X_train, y_train)

        # Log the model
        mlflow.sklearn.log_model(clf, "model")

        # Log parameters and metrics
        accuracy = clf.score(X_test, y_test)
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("accuracy", accuracy)

        print(f"Model accuracy: {accuracy}")

if __name__ == "__main__":
    train_model()
