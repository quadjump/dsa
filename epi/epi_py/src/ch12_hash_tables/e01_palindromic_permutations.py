### 12.1 Test for palindromic permutations ###

"""
A palindrome is a string that reads the same forwards and backwards, e.g., "level", "rotator", and
"foobaraboof".

Write a program to test whether the letters forming a string can be permuted to form a palindrome.
For example, "edified" can be permuted to form "deified".

Hint: Find a simple characterization of strings that can be permuted to form a palindrome.
"""

import collections


def is_palindormic_permutation(xs: str) -> bool:
    """
    To form a palindrome, all but one character must be present an even number of times.

    Use a bitvector to capture odd or even occurences of characters. Then check for at most a
    single set bit to determine whether the string is a palindromic permutation.

    # >>> is_palindormic_permutation("edified")
    # True
    #
    """
    # Check even character counts or single odd character via pop_count
    char_parity: int = 0
    for x in xs:
        char_parity ^= 2 ** ord(x)
    return char_parity == 0 or char_parity & (char_parity - 1) == 0


# Book Solution
def can_form_palindrome(xs: str) -> bool:
    """
    # >>> can_form_palindrome("edified")
    # True
    #
    """
    return sum(v % 2 for v in collections.Counter(xs).values()) <= 1
