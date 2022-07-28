### Increment an arbitrary-precision integer ###

"""
Write a program which takes as input an array of digits encoding a nonnegative decimal integer
D and updates the array to represent the integer D + 1. For example, if the input is (1,2,9) then
you should update the array to (1,3,0). Your algorithm should work even if it is implemented in a
language that has finite-precision arithmetic.

Hint: Experiment with concrete examples.
"""

from typing import List


def increment_digits(digits: List[int], is_carry=True) -> List[int]:
    """
    O(n) time/space.

    A reverse-order array encoding of some integer.

    Pre-conditions:
    - Each digit/element is <=9
    - Number is represented in reverse order (ex. 123 is [3, 2, 1]) 
    
    # >>> increment_digits([3,2,1])
    # [4, 2, 1]
    #
    # >>> increment_digits([9,9,9])
    # [0, 0, 0, 1]
    #
    # >>> increment_digits([9,1,1])
    # [0, 2, 1]
    #
    # >>> increment_digits([1])
    # [2]
    #
    
    """
    match digits, is_carry:
        case digs, False: return digs
        case [], True: return [1]
        case [9, *tail], True: return [0] + increment_digits(tail, is_carry=True)
        case [n, *tail], True if n < 9: return [n+1] + increment_digits(tail, is_carry=False)
        case _: raise Exception('Illegal input: Digit given greater than 9')