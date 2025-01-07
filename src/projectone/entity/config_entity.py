from dataclasses import dataclass
from pathlib import Path
from src.projectone.constants import *
from src.projectone.utils.common import read_yaml, create_directories

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE:str
    unzip_data_dir:Path
    all_schema:dict