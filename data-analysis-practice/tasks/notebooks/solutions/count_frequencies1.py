import pandas as pd
from typing import Union


def count_frequencies(df: pd.DataFrame, col: Union[str, list[str]]) -> pd.DataFrame:
    if isinstance(col, str):
        col = [col]
    df_count = df[col].value_counts().reset_index()
    df_count.columns = col + ['count']
    df_count['freq'] = df_count['count'] / len(df)
    return df_count.set_index(col)
