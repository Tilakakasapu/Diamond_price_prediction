from src.DiamondPricePrediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.DiamondPricePrediction import logger
STAGE_NAME = 'DATA INGESTION STAGE'
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e
