def check_palindromes(m, n):
    """
    Outputs the dictionary that maps each integer from n to m
    inclusively, to the string 'Y' or 'N' depending on whether
    the number is a palindrome ('Y') or not ('N').
    NOTES:
        1. A palindrome is a number that reads the same backward
           as forward.
        2. You can convert to a string to check if an integer
           is a palindrome.
    """
    return {i: 'Y' if str(i) == str(i)[::-1] else 'N' for i in range(m, n+1)}
