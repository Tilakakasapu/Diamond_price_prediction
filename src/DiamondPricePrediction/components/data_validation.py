import os
from src.DiamondPricePrediction import logger
from src.DiamondPricePrediction.entity.config_entity import Data_Validation_Config
import pandas as pd
class Data_Validation:
    def __init__(self,config: Data_Validation_Config):
        self.config = config
    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {validation_status}")
                        f.write(f"current col:{col}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status
        except Exception as e:
            raise e      