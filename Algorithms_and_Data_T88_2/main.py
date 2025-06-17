from typing import List

def raise_to_power(numbers: List[int], powers: List[int]) -> List[int]:
    """
    Raises numbers to the corresponding powers.

    Args:
        numbers: List[int], a list of numbers
        powers: List[int], a list of corresponding powers

    Returns:
        List[int],
            the list of numbers raised to the corresponding powers
    """
    return list(map(lambda x: x[0] ** x[1], zip(numbers, powers)))
