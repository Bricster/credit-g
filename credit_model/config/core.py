# Path setup, and access the config.yml file, datasets folder & trained models
import credit_model

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from pathlib import Path
from typing import Dict, List

from pydantic import BaseModel
from strictyaml import YAML, load

import credit_model

# Project Directories
PACKAGE_ROOT = Path(credit_model.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"
#print(CONFIG_FILE_PATH)

DATASET_DIR = PACKAGE_ROOT / "datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"


class AppConfig(BaseModel):
    """
    Application-level config.
    """

    package_name: str
    training_data_file: str
    pipeline_name: str
    pipeline_save_file: str


class ModelConfig(BaseModel):
    """
    All configuration relevant to model
    training and feature engineering.
    """

    target: str
    features: List[str]
    unused_fields: List[str]
    
    checking_status: str
    duration: float
    credit_history: str
    purpose: str
    credit_amount: float
    savings_status: str
    employment: str
    installment_commitment: float
    personal_status: str
    other_parties: str
    residence_since: float
    property_magnitude: str
    age: float
    other_payment_plans: str
    housing: str
    existing_credits: float
    job: str
    num_dependents: float
        
    checking_mapping: Dict[str, int]
    credit_mappings: Dict[str, int]
    purpose_mappings: Dict[str, int]
    savings_mappings: Dict[str, int]
    employment_mappings: Dict[str, int]
    party_mappings: Dict[str, int]
    personal_mappings: Dict[str, int]
    property_mappings: Dict[str, int]
    other_mapping: Dict[str, int]
    housing_mappings: Dict[str, int]
    job_mappings: Dict[str, int]


    test_size:float
    random_state: int
    n_estimators: int
    max_depth: int


class Config(BaseModel):
    """Master config object."""

    app_config: AppConfig
    model_config: ModelConfig


def find_config_file() -> Path:
    """Locate the configuration file."""
    
    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH
    
    raise Exception(f"Config not found at {CONFIG_FILE_PATH!r}")


def fetch_config_from_yaml(cfg_path: Path = None) -> YAML:
    """Parse YAML containing the package configuration."""

    if not cfg_path:
        cfg_path = find_config_file()

    if cfg_path:
        with open(cfg_path, "r") as conf_file:
            parsed_config = load(conf_file.read())
            return parsed_config      
    raise OSError(f"Did not find config file at path: {cfg_path}")


def create_and_validate_config(parsed_config: YAML = None) -> Config:
    """Run validation on config values."""
    if parsed_config is None:
        parsed_config = fetch_config_from_yaml()

    # specify the data attribute from the strictyaml YAML type.
    _config = Config(
        app_config = AppConfig(**parsed_config.data),
        model_config = ModelConfig(**parsed_config.data),
    )

    return _config


config = create_and_validate_config()
