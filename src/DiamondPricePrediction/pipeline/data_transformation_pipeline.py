from src.DiamondPricePrediction.config.configuration import ConfigurationManager
from src.DiamondPricePrediction.components.data_transformation import Data_Transformation
from src.DiamondPricePrediction import logger
STAGE_NAME= "data transformation"
class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config= ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = Data_Transformation(config=data_transformation_config)
        data_transformation.train_test_spliting()
if __name__=='__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e