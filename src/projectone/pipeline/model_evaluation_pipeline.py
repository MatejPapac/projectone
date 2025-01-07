from src.projectone.config.configuration import ConfigurationManager
from src.projectone.components.model_evaluation import ModelEvaluation
from src.projectone import logger

STAGE_NAME = 'Model evaluation stage'

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config =config.get_model_evaluation_config()
        model_evaluation=ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()