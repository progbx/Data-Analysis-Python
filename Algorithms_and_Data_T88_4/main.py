def filter_out_articles(text: str) -> str:
    """
    Filters out English articles from text.

    Args:
        text: str,
            input text - a sequence of English words separated
            by a single whitespace that does not contain punctuation.

    Returns:
        str, the text obtained from the input by removing articles.
    """
    # Define the set of articles (case-insensitive)
    articles = {"a", "an", "the"}

    # Split the text into words, filter out the articles using filter function
    filtered_words = filter(lambda word: word.lower() not in articles, text.split())

    # Join the filtered words back into a string and return
    return " ".join(filtered_words)
