"""Template for programming assignment:
Convert roman number to integer number"""


def roman_to_integer(roman: str) -> int:
    """Converts a Roman numeral to an integer.

    Args:
        roman: str, Roman numeral
    Returns:
        int, integer representation of a Roman numeral
    """
    roman_to_int_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman):
        current_value = roman_to_int_map[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value

    return total

