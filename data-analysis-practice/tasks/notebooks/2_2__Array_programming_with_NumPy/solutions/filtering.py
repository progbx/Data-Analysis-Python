from typing import List
import numpy as np


def filter_data(data: np.ndarray, rules_to_ignore: List[int] = []) -> np.ndarray:
    """Filters a given array based on the set of rules described below.

    Rules (should be applied sequentially):
    0) All rows that contain NaNs (np.nan) should be removed.
    1) All rows in which the largest element is in a column with an odd index should be removed.
    2) All columns in which the number of negative elements is larger than the number of positive elements should be removed.
    3)
      3.0) For each column, you should calculate the standard deviation of elements (std_col_i).
      3.1) Calculate the mean of the standard deviations from 3.0 (mu_std_cols).
      3.2) All columns in which more than 10 elements are larger than `2 * mu_std_cols` should be removed.

    Args:
        data: np.ndarray, a given 2d array
        rules_to_ignore: List[int], a list of rules that should be ignored (from {0, 1, 2, 3})
    Returns:
        np.ndarray, the resulting array
    """
    result = data.copy()
    
    # Rule 0: Remove rows with NaNs
    if 0 not in rules_to_ignore:
        result = result[~np.isnan(result).any(axis=1)]
    
    # Rule 1: Remove rows where largest element is in a column with odd index
    if 1 not in rules_to_ignore:
        max_indices = np.argmax(result, axis=1)
        result = result[max_indices % 2 == 0]
    
    # Rule 2: Remove columns where #negative > #positive
    if 2 not in rules_to_ignore:
        pos_count = np.sum(result > 0, axis=0)
        neg_count = np.sum(result < 0, axis=0)
        result = result[:, pos_count >= neg_count]
    
    # Rule 3: Remove columns with more than 10 elements > 2*avg_std
    if 3 not in rules_to_ignore:
        # Calculate std for each column
        std_cols = np.std(result, axis=0)
        # Calculate mean of std values
        mu_std_cols = np.mean(std_cols)
        # Count elements in each column that are > 2*mu_std_cols
        large_elements_count = np.sum(result > 2 * mu_std_cols, axis=0)
        # Keep columns where count <= 10
        result = result[:, large_elements_count <= 10]
    
    return result
