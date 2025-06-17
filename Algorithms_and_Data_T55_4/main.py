def pell_numbers():
    """Generates Pell numbers"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, 2 * b + a
