from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    local_file_dir: Path
@dataclass(frozen=True)
class Data_Validation_Config:
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: str
    all_schema: dict
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path 
@dataclass(frozen=True)
class ModelTraining:
    root_dir: Path
    train_data: str
    test_data: str
    