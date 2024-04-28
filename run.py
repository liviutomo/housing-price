import mlflow

experiment_name = "ElasticNet"
entry_point = "Training"

mlflow.set_tracking_uri("http://ec2-13-60-64-97.eu-north-1.compute.amazonaws.com:5000/")

mlflow.projects.run(
    uri=".",
    entry_point=entry_point,
    experiment_name=experiment_name,
    env_manager="conda"
)