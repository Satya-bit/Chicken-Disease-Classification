# Data Ingestion config/Entity which helps defining custom written type of function using entity


#The use of a config entity file in modular coding enhances the flexibility, maintainability, and scalability of your software by separating configuration from code. 
# It provides a centralized, reusable, and secure way to manage application settings, making it easier to adapt to different environments and requirements.


#Configuration refers to the process of setting up or arranging the components of a system or software in a particular way to achieve desired functionality.
# It involves defining and customizing the parameters, settings, and options that control how a system operates or how software behaves.

from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path



@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
    
    
@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path