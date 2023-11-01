import os
from src.DiamondPricePrediction import logger
from src.DiamondPricePrediction.entity.config_entity import DataIngestionConfig
class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config
