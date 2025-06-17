import pandas as pd
from typing import Union


def describe_numericals(
    df: pd.DataFrame,
    col: Union[str, list[str]]
) -> pd.DataFrame:
    """
    Describe each specified numerical column with five statistics:
    - median
    - 0.25 quantile (Q1)
    - 0.75 quantile (Q3)
    - lower whisker (lower)
    - upper whisker (upper)

    Here:
        - The lower whisker is Q1 - 1.5 * (Q3 - Q1)
        - The upper whisker is Q3 + 1.5 * (Q3 - Q1)

    Args:
        df: pd.DataFrame, an input dataframe
        col: list[str], columns to describe
    Returns:
        pd.DataFrame
            A dataframe of the shape (5, len(col)) that contains
            the descriptive statistics mentioned above. Its
            index should be ["lower", "Q1", "median", "Q3", "upper"]
    """
    if isinstance(col, str):
        col = [col]

    descr = pd.DataFrame(index=["lower", "Q1", "median", "Q3", "upper"])
    
    for c in col:
        descr[c] = [
            df[c].quantile(0.25) - 1.5 * (df[c].quantile(0.75) - df[c].quantile(0.25)),
            df[c].quantile(0.25),
            df[c].median(),
            df[c].quantile(0.75),
            df[c].quantile(0.75) + 1.5 * (df[c].quantile(0.75) - df[c].quantile(0.25))
        ]
    
    return descr
