from src.projectone import logger
from src.projectone.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.projectone.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.projectone.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.projectone.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.projectone.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
STAGE_NAME = 'Data Ingestion stage'

try:
        logger.info(f'>>>> stage {STAGE_NAME} started <<<<')
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion() 
        logger.info(f'>>>> stage {STAGE_NAME} completed <<<< \n\nx=======x')
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = 'Data Validation stage'

try:
        logger.info(f'>>>> stage {STAGE_NAME} started <<<<')
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation() 
        logger.info(f'>>>> stage {STAGE_NAME} completed <<<< \n\nx=======x')
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = 'Data Transformation stage'

try:
        logger.info(f'>>>> stage {STAGE_NAME} started <<<<')
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation() 
        logger.info(f'>>>> stage {STAGE_NAME} completed <<<< \n\nx=======x')
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = 'Model Trainer stage'

try:
        logger.info(f'>>>> stage {STAGE_NAME} started <<<<')
        obj=ModelTrainerPipeline()
        obj.initiate_model_training()
        logger.info(f'>>>> stage {STAGE_NAME} completed <<<< \n\nx=======x')
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = 'Model evaluation stage'

try:
        logger.info(f'>>>> stage {STAGE_NAME} started <<<<')
        obj=ModelEvaluationPipeline()
        obj.initate_model_evaluation()
        logger.info(f'>>>> stage {STAGE_NAME} completed <<<< \n\nx=======x')
except Exception as e:
        logger.exception(e)
        raise e
        



