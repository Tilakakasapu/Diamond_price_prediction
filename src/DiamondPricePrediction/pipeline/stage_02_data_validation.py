from src.DiamondPricePrediction.components.data_validation import Data_Validation
from src.DiamondPricePrediction.config.configuration import ConfigurationManager
from src.DiamondPricePrediction import logger
STAGE_NAME = 'data_validation_stage'
class Data_validation_Training_Pipeline():
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = Data_Validation(config=data_validation_config)
        data_validation.validate_all_columns()
if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = Data_validation_Training_Pipeline()
        obj.main()
        logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e
    