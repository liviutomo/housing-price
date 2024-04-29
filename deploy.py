import mlflow.sagemaker
from mlflow.deployments import get_deploy_client

endpoint_name="prod:endpoint"
model_uri="s3://mlops-mlflow-project-artifacts/1/75febeca22f94353a72b1efc740abb6e/artifacts/ElasticNet"

# Define your configuration parameters as a dictionary
config = {
    "execution_role_arn": "arn:aws:iam::891377058700:role/mlops-project-housing-price-role",
    "bucket_name": "mlops-mlflow-project-artifacts",
    "image_url": "8891377058700.dkr.ecr.us-east-1.amazonaws.com/elastic-the-best:2.12.1",
    "region_name": "us-east-1",
    "archive": False,
    "instance_type": "ml.m5.xlarge",
    "instance_count": 1,
    "synchronous": True
}

# Initialize a deployment client for SageMaker
client = get_deploy_client("sagemaker")

# Create the deployment
client.create_deployment(
    name=endpoint_name,
    model_uri=model_uri,
    flavor="python_function",
    config=config,
)
