"""Template for programming assignment:
Convert integer number to roman number"""


def integer_to_roman(integer: int) -> str:
    """Converts an integer to a Roman numeral.

    Examples:
        3 -> "III"
        58 -> "LVIII"
        1994 -> "MCMXCIV"

    Args:
        integer: str, integer number
    Returns:
        str, string representation of a Roman numeral
    """
    value_symbol_pairs = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    roman = []

    for value, symbol in value_symbol_pairs:
        while integer >= value:
            roman.append(symbol)
            integer -= value

    return ''.join(roman)

