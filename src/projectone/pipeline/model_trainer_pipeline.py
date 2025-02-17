from src.projectone.config.configuration import ConfigurationManager
from src.projectone.components.model_trainer import ModelTrainer
from src.projectone import logger


STAGE_NAME='Model Trainer stage'

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()

    
    
    
if __name__ == '__main__':
     try:
        logger.info(f'>>>> stage {STAGE_NAME} started <<<<')
        obj = ModelTrainerPipeline()
        obj.initiate_model_training() 
        logger.info(f'>>>> stage {STAGE_NAME} completed <<<< \n\nx=======x')
     except Exception as e:
        logger.exception(e)
        raise e
    