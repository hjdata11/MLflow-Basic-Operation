import dagshub
dagshub.init(repo_owner='hjdata11', repo_name='MLflow-Basic-Operation', mlflow=True)

import os
os.environ['MLFLOW_TRACKING_USERNAME'] = 'hjdata11'
os.environ['MLFLOW_TRACKING_PASSWORD'] = '86889e51af823ef037e4e1a6d0998986a55d3468'
os.environ['MLFLOW_TRACKING_URI'] = 'https://dagshub.com/hjdata11/MLflow-Basic-Operation.mlflow'