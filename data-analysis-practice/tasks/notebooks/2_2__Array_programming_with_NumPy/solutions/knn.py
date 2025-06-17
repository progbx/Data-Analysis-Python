import numpy as np


def find_knn(points_a: np.ndarray, points_b: np.ndarray, k: int) -> np.ndarray:
    """For the given sets of points A and B (in N-dimensional space) returns the indices of the K closest points from B for each point from A.

    It is guaranteed that:
    1) points_a.shape == (k1, N), N >= 1, k1 >= 1
    2) points_b.shape == (k2, N), k2 >= k >= 1

    NOTE: The resulting array should have a shape of (k1, k).
    NOTE: You should use L2 metric to calculate the distances between points.
    NOTE: You should use vectorization; for-loops are too slow.
    
    Args:
        points_a: np.ndarray, the first set of points (A)
        points_b: np.ndarray, the second set of points (B)
        k: int, the number of nearest neighbor indices to return for each point from A
    Returns:
        np.ndarray, the resulting array
    """
    # Compute pairwise squared distances (vectorized)
    # Reshape points to enable broadcasting
    a_expanded = np.expand_dims(points_a, axis=1)  # Shape: (k1, 1, N)
    b_expanded = np.expand_dims(points_b, axis=0)  # Shape: (1, k2, N)
    
    # Calculate squared Euclidean distances
    squared_distances = np.sum((a_expanded - b_expanded) ** 2, axis=2)  # Shape: (k1, k2)
    
    # Find indices of k smallest distances for each point in A
    return np.argsort(squared_distances, axis=1)[:, :k]
