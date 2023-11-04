from src.DiamondPricePrediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.DiamondPricePrediction import logger
from src.DiamondPricePrediction.pipeline.stage_02_data_validation import Data_validation_Training_Pipeline
from src.DiamondPricePrediction.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.DiamondPricePrediction.pipeline.stage_04_model_training import ModelTrainingPipeline
STAGE_NAME = 'DATA INGESTION STAGE'
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e
STAGE_NAME='DATA VALIDATION'
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj = Data_validation_Training_Pipeline()
    obj.main()
    logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e
STAGE_NAME = "Data Transformation"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e
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
    