import mlflow

model_name = "RandomForestModel"
model_uri = f"runs:/{mlflow.active_run().info.run_uuid}/model"
mlflow.register_model(model_uri, model_name)

# Promote the model to the 'Production' stage
client = mlflow.tracking.MlflowClient()
client.transition_model_version_stage(
    name=model_name,
    version=1,
    stage="Production"
)
