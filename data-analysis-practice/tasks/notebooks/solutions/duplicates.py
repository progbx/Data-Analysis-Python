import uuid
import numpy as np
import pandas as pd


def remove_duplicates(df: pd.DataFrame, tol: float=1e-5) -> pd.DataFrame:
    """Removes duplicated rows from a given dataframe.

    NOTE: The `tol` parameter should be used to compare values in numerical columns (|a - b| < tol => (a == b)).
    NOTE: If a dataframe has three rows [`a`, `b`,`c`], `a == b` and `b == c` -> only `a` should be kept. 
    NOTE: Assume that `NaN == NaN` is the expected behavior.
    NOTE: If two rows are `equal`, please keep the row with the lowest index.
    NOTE: It is not allowed to change the order of rows in the resulting dataframe.
    NOTE: It is not allowed to change the indices in the resulting dataframe, meaning that the initial order of rows
    (and the corresponding indices) should stay the same.

    Args:
        df: pd.DataFrame, a dataframe for deduplication.
        tol: float, the precision with which numerical values should be compared.
    Returns:
        pd.DataFrame, the resulting dataframe after deduplication.
    """
    df_copy = df.copy()
    
    # Convert numerical columns to object dtype for easier comparison with tolerance
    for col in df_copy.select_dtypes(include='number'):
        df_copy[col] = df_copy[col].round(decimals=-int(np.log10(tol)))

    # No need to add index, use the implicit index for drop_duplicates
    df_copy = df_copy.drop_duplicates(keep='first') 
    
    # Reset the index to match original DataFrame
    df_copy = df_copy.reset_index(drop=True)

    return df_copy
