from typing import List, Tuple

def sort_points(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Sorts a list of points on a plane in descending order
    of their distance from the origin. If two points are equally
    distant from the origin, return the leftmost one first.
    If two points are equally distant from the origin and lie on
    the same vertical, return the bottom one first.

    Args:
        points: List[Tuple[int, int]],
            list of tuples of the form (x, y), where x and y are
            coordinates of a point on a plane.

    Returns:
        List[Tuple[int, int]], the sorted list of points
    """
    return sorted(points, key=lambda p: (-p[0]**2 - p[1]**2, p[0], p[1]))

