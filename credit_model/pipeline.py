import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

from credit_model.config.core import config
from credit_model.processing.features import Mapper


credit_pipe = Pipeline([
    ######### Mapper ###########
    ('map_checking', Mapper(variable = config.model_config.checking_status, mappings = config.model_config.checking_mapping)),
    
    ('map_credit', Mapper(variable = config.model_config.credit_history, mappings = config.model_config.credit_mappings)),
    
    ('map_purpose', Mapper(variable = config.model_config.purpose, mappings = config.model_config.purpose_mappings)),
    
    ('map_saving', Mapper(variable = config.model_config.savings_status, mappings = config.model_config.savings_mappings)),
    
    ('map_emp', Mapper(variable = config.model_config.employment, mappings = config.model_config.employment_mappings)),
    
    ('map_otherparty', Mapper(variable = config.model_config.other_parties, mappings = config.model_config.party_mappings)),
    
    ('map_personal', Mapper(variable = config.model_config.personal_status, mappings = config.model_config.personal_mappings)),
    
    ('map_property', Mapper(variable = config.model_config.property_magnitude, mappings = config.model_config.property_mappings)),

    ('map_otherpayment', Mapper(variable = config.model_config.other_payment_plans, mappings = config.model_config.other_mapping)),

    ('map_housing', Mapper(variable = config.model_config.housing, mappings = config.model_config.housing_mappings)),

    ('map_job', Mapper(variable = config.model_config.job, mappings = config.model_config.job_mappings)),

    # Scale features
    ('scaler', StandardScaler()),
    
    # Regressor
    ('model_rf', RandomForestRegressor(n_estimators = config.model_config.n_estimators, 
                                       max_depth = config.model_config.max_depth,
                                      random_state = config.model_config.random_state))
    
    ])
