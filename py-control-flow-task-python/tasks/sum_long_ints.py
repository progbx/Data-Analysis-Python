"""Template for programming assignment: sum two long numbers"""
from typing import List


def sum_long_integers(number_1: List[int], number_2: List[int]) -> List[int]:
    """Returns the sum of two long numbers represented as
    lists of their digits in the same form.

    Examples:
        [2, 1] + [3, 6] = [5, 7], since 21 + 36 = 57
        [1, 2] + [9] = [2, 1], since 12 + 9 = 21

    Args:
        number_1: List[int], the list of digits of the first term
        number_2: List[int], the list of digits of the second term
    Returns:
        List[int], the list of digits of the sum of input terms
    """
    result = []
    carry = 0
    max_length = max(len(number_1), len(number_2))

    for i in range(max_length):
        digit_1 = number_1[-(i + 1)] if i < len(number_1) else 0
        digit_2 = number_2[-(i + 1)] if i < len(number_2) else 0

        total = digit_1 + digit_2 + carry
        carry = total // 10
        result.append(total % 10)

    if carry:
        result.append(carry)

    return result[::-1]
