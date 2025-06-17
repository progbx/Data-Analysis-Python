import re
from typing import List

# Define custom exceptions
class InputFormatError(ValueError):
    """Raised when the input text contains invalid characters or formatting."""
    pass

class SplitError(ValueError):
    """Raised when the text cannot be split into the required number of parts."""
    pass

def split_text(text: str, n_parts: int) -> List[str]:
    """
    Splits the input text into the specified number of parts so that each
    part (except, possibly, for the last one) contains the same
    number of words.

    Args:
        text : str
            Text to be split, must contain words consisting of
            English letters that are separated by one whitespace.
        n_parts : int
            The number of text parts in the output list, must be
            a positive integer.

    Raises:
        InputFormatError : If the text contains characters other than
            English letters and whitespaces, or the words are separated
            by more than one whitespace.
        ValueError : If the number of text parts is not positive.
        SplitError : If the split cannot be done, i.e., the number of
            words in the text is less than the number of text parts.

    Returns:
        text_parts : List[str]
            The list of text parts of the length n_parts.
    """
    # Validate the number of parts
    if n_parts <= 0:
        raise ValueError("The number of text parts must be a positive integer.")

    # Check for invalid characters (only English letters and spaces allowed)
    if not re.fullmatch(r"[A-Za-z ]+", text):
        raise InputFormatError("Text contains invalid characters.")

    # Check for multiple consecutive spaces
    if "  " in text:
        raise InputFormatError("Text contains multiple consecutive spaces.")

    # Split the text into words
    words = text.split()

    # Check if we can split into the required parts
    if len(words) < n_parts:
        raise SplitError("Cannot split text into the specified number of parts.")

    # Split words into n_parts approximately evenly
    avg_part_size = len(words) // n_parts
    remainder = len(words) % n_parts

    parts = []
    index = 0
    for i in range(n_parts):
        part_size = avg_part_size + (1 if i < remainder else 0)
        parts.append(" ".join(words[index:index + part_size]))
        index += part_size

    return parts
