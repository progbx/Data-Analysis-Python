import string
import pandas as pd


def parse_numeric_column(df: pd.DataFrame, target_columns: str) -> pd.DataFrame:
    df[target_columns] = df[target_columns].apply(lambda x: ''.join(c for c in str(x) if c.isdigit() or c == '.' or c == '-') or '0')
    df[target_columns] = df[target_columns].astype('float32')
    return df
