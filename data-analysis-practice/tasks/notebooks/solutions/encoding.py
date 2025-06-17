from typing import Dict, Union
from dataclasses import dataclass
import pandas as pd

@dataclass
class LabelEncodingParameters:
    # Defines a mapping that should be used for label encoding
    mapping: Dict[str, int]
    remove_original_attribute: bool = False


@dataclass
class OneHotEncodingParameters:
    # The refix that should be used for one-hot encoding so that resulting column names are in the following format:
    # {prefix}_{value}
    prefix: str
    remove_original_attribute: bool = False


def encode_categorical_attributes(df: pd.DataFrame, parameters: Dict[str, Union[LabelEncodingParameters, OneHotEncodingParameters]]) -> pd.DataFrame:
    for column, param in parameters.items():
        if isinstance(param, LabelEncodingParameters):
            df[column + '_label_encoding'] = df[column].map(param.mapping)
            if param.remove_original_attribute:
                df = df.drop(column, axis=1)
        elif isinstance(param, OneHotEncodingParameters):
            one_hot = pd.get_dummies(df[column], prefix=param.prefix).astype(int)
            df = pd.concat([df, one_hot], axis=1)
            if param.remove_original_attribute:
                df = df.drop(column, axis=1)
    return df
