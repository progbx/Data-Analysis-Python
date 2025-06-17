import numpy as np
import pandas as pd


def handle_missing_values(
    df: pd.DataFrame, 
    percent_missing_per_row: float = 0.5,
    percent_missing_per_column: float = 0.5,
) -> pd.DataFrame:
    """Handles missing values in a given dataframe according to the instructions below.

    Instructions for handling missing values (the steps below should be executed sequentially, one by one):
    0) Remove rows where the percentage of missing values is greater than `percent_missing_per_row`.
    1) Remove columns where the percentage of missing values is greater than `percent_missing_per_column`.
    2) For each categorical column impute missing values with the string "missing".
    3) For each numerical column impute missing values with the corresponding column-wise means.

    NOTE: It is not allowed to change the indices in the result dataframe, meaning that the initial order of rows
    (and the corresponding indices) should stay the same.
    
    HINT: You may find `.loc/.iloc` indexing useful. 

    Args:
        df: pd.DataFrame, a dataframe for handling missing values.
        percent_missing_per_row: float, the threshold for removing rows.
        percent_missing_per_column: float, the threshold for removing columns.
    Returns:
        pd.DataFrame, the resulting dataframe.
    """
    df_copy = df.copy()

    # 0) Remove rows with high missing value percentage
    df_copy = df_copy[df_copy.isnull().sum(axis=1) / df_copy.shape[1] <= percent_missing_per_row]
    df_copy = df_copy.reset_index(drop=True) # Reset index to avoid issues

    # 1) Remove columns with high missing value percentage
    df_copy = df_copy.loc[:, df_copy.isnull().sum(axis=0) / df_copy.shape[0] <= percent_missing_per_column]

    # 2) Impute missing values in categorical columns
    for col in df_copy.select_dtypes(include='object'):
        df_copy[col] = df_copy[col].fillna("missing")

    # 3) Impute missing values in numerical columns
    for col in df_copy.select_dtypes(include='number'):
        df_copy[col] = df_copy[col].fillna(df_copy[col].mean())
    
    return df_copy