import pandas as pd
import numpy as np

def calculate_correlation(
    df: pd.DataFrame,
    threshold: float,
) -> pd.DataFrame:
    """
    Calculate the correlation matrix for a given dataframe, dropping columns and rows where 
    the correlation with any other variables isn't greater than `threshold` by modulus.

    Args:
        df: pd.DataFrame, an input dataframe
        threshold: int, an input threshold
    Returns:
        pd.DataFrame
            A dataframe that contains a submatrix of the correlation matrix
    """

    corr_matrix = df.corr()
    cols_to_keep = []

    for col in corr_matrix:
        keep_col = False
        for row in corr_matrix:
            if col != row and abs(corr_matrix[col][row]) > threshold:
                keep_col = True
                break
        if keep_col:
            cols_to_keep.append(col)

    return corr_matrix.loc[cols_to_keep, cols_to_keep]
