def compute_jaccard_index(s1, s2):
    intersection_size = len(s1 & s2)
    union_size = len(s1 | s2)
    jaccard = intersection_size / union_size
    return round(jaccard, 6)