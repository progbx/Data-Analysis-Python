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
    # Use broadcasting to compute the pairwise distances
    distances = np.linalg.norm(points_a[:, np.newaxis] - points_b, axis=2)
    
    # Find the indices of the k smallest distances for each point in points_a
    knn_indices = np.argsort(distances, axis=1)[:, :k]
    
    return knn_indices