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
    filtered_data = data.copy()

    if 0 not in rules_to_ignore:
        filtered_data = filtered_data[~np.isnan(filtered_data).any(axis=1)]

    if 1 not in rules_to_ignore:
        max_indices = np.argmax(filtered_data, axis=1)
        filtered_data = filtered_data[max_indices % 2 == 0]

    if 2 not in rules_to_ignore:
        negative_counts = (filtered_data < 0).sum(axis=0)
        positive_counts = (filtered_data > 0).sum(axis=0)
        filtered_data = filtered_data[:, negative_counts <= positive_counts]

    if 3 not in rules_to_ignore:
        std_cols = np.std(filtered_data, axis=0)
        mu_std_cols = np.mean(std_cols)
        large_element_counts = (filtered_data > 2 * mu_std_cols).sum(axis=0)
        filtered_data = filtered_data[:, large_element_counts <= 10]

    return filtered_data