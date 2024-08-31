from typing import Any, List, Optional
import datetime

from pydantic import BaseModel
from credit_model.processing.validation import DataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    #predictions: Optional[List[int]]
    predictions: Optional[int]


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                "checking_status": "no checking",   
                "duration": 12, 
                "credit_history": "critical/other existing credit",
                "purpose": "education", 
                "credit_amount": 2096,
                "savings_status": "<100",
                "employment": "4<=X<7",
                "installment_commitment": 2,
                "personal_status": "male single",
                "other_parties": "none",	
                "residence_since": 3,
                "property_magnitude": "real estate",
                "age": 3,
                "other_payment_plans": "none",
                "housing": "own",
                "existing_credits": 2,
                "job": "unskilled resident",
                "num_dependents": 2,
                    }
                ]
            }
        }
