import pandas as pd


def standardize_numericals(df: pd.DataFrame, col: list[str]) -> pd.DataFrame:
    """
    Standardize the specified columns in a dataframe by
    subtracting the mean and dividing the result by the standard
    deviation.

    NOTE: Please use the parameter ddof=0 for the std function
    in your implementation.

    Args:
        df: pd.DataFrame, an input dataframe
        col: list[str], columns to standardize
    Returns:
        pd.DataFrame
            An updated dataframe where the specified columns
            have a mean of 0 and a unit variance
    """
    df_copy = df.copy()
    for c in col:
        df_copy[c] = (df_copy[c] - df_copy[c].mean()) / df_copy[c].std(ddof=0)
    return df_copy
