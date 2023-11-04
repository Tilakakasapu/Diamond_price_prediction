from src.DiamondPricePrediction.constants import *
from src.DiamondPricePrediction.utils.common import read_yaml,create_directories
from src.DiamondPricePrediction.entity.config_entity import DataIngestionConfig,Data_Validation_Config,DataTransformationConfig,ModelTraining
class ConfigurationManager:
    def __init__(
        self,
        config_filepath= CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath= SCHEMA_FILE_PATH):
        self.config= read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        create_directories ([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            local_file_dir= config.local_file_dir,
        )
        return data_ingestion_config
    def get_data_validation_config(self)->Data_Validation_Config:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])
        data_validation_config = Data_Validation_Config(
        root_dir= config.root_dir,
        STATUS_FILE= config.STATUS_FILE,
        unzip_data_dir= config.unzip_data_dir,
        all_schema=schema
        )
        return data_validation_config
    def get_data_transformation_config(self)-> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path= config.data_path
        )
        return data_transformation_config
    def model_training_config(self)->ModelTraining:
        config  = self.config.model_training
        create_directories([config.root_dir])
        model_training_config  =ModelTraining(
            root_dir = config.root_dir,
            train_data= config.train_data,
            test_data = config.test_data
        )
        return model_training_config