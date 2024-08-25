import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from typing import List, Optional, Tuple, Union

from datetime import datetime
import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from credit_model.config.core import config
from credit_model.processing.data_manager import pre_pipeline_preparation


def validate_inputs(*, input_df: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    pre_processed = pre_pipeline_preparation(data_frame = input_df)
    validated_data = pre_processed[config.model_config.features].copy()
    errors = None

    try:
        # replace numpy nans so that pydantic can validate
        MultipleDataInputs(
            inputs = validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return validated_data, errors


class DataInputSchema(BaseModel):
    checking_status: Optional[str]
    duration: Optional[int]
    hr: Optional[str]
    credit_history: Optional[str]
    purpose: Optional[str]
    credit_amount: Optional[int]
    savings_status: Optional[str]
    employment: Optional[str]
    installment_commitment: Optional[str]
    personal_status: Optional[str]
    other_parties: Optional[str]
    residence_since: Optional[str]
    property_magnitude: Optional[str]
    age: Optional[int]
    other_payment_plans: Optional[str]
    housing: Optional[str]
    existing_credits: Optional[str]
    job: Optional[str]
    num_dependents: Optional[str]


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]