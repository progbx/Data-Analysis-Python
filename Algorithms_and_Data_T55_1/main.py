def generate_multiplication_matrix(m, n):
    """
    Generate a multiplication matrix as a list of m lists,
    each of the size n, containing the product of every number from 1 to m
    with every number from 1 to n.
    NOTE: Your solution must use a list comprehension and
    occupy one line of code.
    """
    return [[(i+1)*(j+1) for j in range(n)] for i in range(m)]