import numpy as np
import pandas as pd


def identify_outliers(df: pd.DataFrame) -> pd.DataFrame:
    df_copy = df.copy()
    df_copy['outliers_count'] = 0
    for col in df_copy.select_dtypes([np.number]).columns:
        Q1 = df_copy[col].quantile(0.25)
        Q3 = df_copy[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df_copy['outliers_count'] += ((df_copy[col] < lower_bound) | (df_copy[col] > upper_bound)).astype(int)
    return df_copy
