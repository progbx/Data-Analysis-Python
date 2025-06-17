import pandas as pd

def count_frequencies(df: pd.DataFrame, col_x: str, col_y: str) -> pd.DataFrame:
    df = df.explode(col_x).explode(col_y)
    count_df = df.groupby([col_x, col_y]).size().reset_index(name='count')
    count_df['freq'] = count_df['count'] / len(df)
    count_df.columns = ['cat_x', 'cat_y', 'count', 'freq']  # Set the correct column names
    return count_df

