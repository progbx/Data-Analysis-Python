import pandas as pd


def describe_categoricals_by_numericals(
    df: pd.DataFrame, 
    col_cat: str, 
    col_num: str
) -> pd.DataFrame:
   
    descr_df = pd.DataFrame(index=["lower", "Q1", "median", "Q3", "upper"], columns=df[col_cat].unique(), dtype=float) 
    for i in df[col_cat].unique():
      descr_df[i]['median'] = df[df[col_cat] == i][col_num].median()
      descr_df[i]['Q1'] = df[df[col_cat] == i][col_num].quantile(0.25)
      descr_df[i]['Q3'] = df[df[col_cat] == i][col_num].quantile(0.75)
      descr_df[i]['lower'] = descr_df[i]['Q1'] - 1.5 * (descr_df[i]['Q3'] - descr_df[i]['Q1'])
      descr_df[i]['upper'] = descr_df[i]['Q3'] + 1.5 * (descr_df[i]['Q3'] - descr_df[i]['Q1'])
    return descr_df
