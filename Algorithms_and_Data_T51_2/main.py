def dict_symmetric_difference(d1, d2):
    d = {}
    keys_diff = d1.keys() ^ d2.keys()
    for key in keys_diff:
        if key in d1:
            d[key] = d1[key]
        elif key in d2:
            d[key] = d2[key]
    return d