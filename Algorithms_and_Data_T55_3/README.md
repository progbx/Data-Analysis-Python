__Task description__

A _palindrome_ is a number that reads the same backward and forward. For every integer number from __m__ to __n__ inclusively, return "Y" if the number is a palindrome and "N" if it is not. Your output should be a dictionary that maps integers from __m__ to __n__ to the strings "Y" or "N."

_Note 1_: You can convert to a string to check if an integer is a palindrome.

_Note 2_: Your solution must occupy one line of code by using a list comprehension.

<br>

__Test data sets examples__

| № | Input data | Expected output |
|----------|----------|----------|
| 1    | 10000,10001    | {10000: 'N', 10001: 'Y'}     |
| 2    | 2000000,2000005  | {2000000: 'N', 2000001: 'N', 2000002: 'Y', 2000003: 'N', 2000004: 'N', 2000005: 'N'}     |