def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    dict = {}
    for sentence in sentences:
        for token in sentence:
            if token in dict:
                dict[token] += 1
            else:
                dict[token] = 1
    return dict