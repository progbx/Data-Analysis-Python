from typing import List
from functools import reduce

def transform_sentences_to_words(sentences: List[str]) -> List[str]:
    """
    Transforms a list of sentences (strings) into a flat list
    of all the words (strings) found in the sentences in the order
    they appear. A word is any sequence of subsequent non-whitespace
    characters.

    Args:
        sentences: List[str], a list of sentences

    Returns:
        List[str], the list of words in the order
            they appear in the sentences
    """
    return reduce(lambda x, y: x + y, map(lambda sentence: sentence.split(), sentences))
