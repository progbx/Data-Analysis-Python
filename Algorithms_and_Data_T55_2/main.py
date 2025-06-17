def select_palindromes(m, n):
    """
    Outputs the list of all palindromes found among integers
    from m to n inclusively.
    NOTES:
        1. A palindrome is a number that reads the same backward
           and forward.
        2. You can convert to a string to check if an integer
           is a palindrome.
    """
    return [i for i in range(m, n+1) if str(i) == str(i)[::-1]]
