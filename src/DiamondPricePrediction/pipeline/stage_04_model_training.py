from src.DiamondPricePrediction.components.model_training import Model_Training
from src.DiamondPricePrediction.config.configuration import ConfigurationManager
from  src.DiamondPricePrediction import logger
STAGE_NAME = 'Model Training'
class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        Model_Train_config = config.model_training_config()
        Model_Training_1 = Model_Training(config= Model_Train_config)
        Model_Training_1.train_model()
STAGE_NAME = 'Model Training'
if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e
    