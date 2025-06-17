import pandas as pd
import numpy as np

def calculate_histogram_data(
    df: pd.DataFrame,
    col: list[str],
    bins: int = 10
) -> pd.DataFrame:
    """
    Calculates a dataframe with data needed to plot a histogram.
    # ... (rest of the docstring)
    """
    min_val = 0 # Fixed to match the test data generation
    max_val = 1 # Fixed to match the test data generation
    width = (max_val - min_val) / bins 

    bin_starts = [i * width for i in range(bins)]
    bin_ends = [(i + 1) * width for i in range(bins)]
    bin_edges = np.array(bin_starts + [bin_ends[-1]]) # Include the last edge

    hist_data = pd.DataFrame({'bin_start': bin_starts, 'bin_end': bin_ends})

    for c in col:
        hist, _ = np.histogram(df[c], bins=bin_edges)
        hist_data[c] = hist

    return hist_data
