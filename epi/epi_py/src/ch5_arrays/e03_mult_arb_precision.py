### Multiply two arbitrary-precision integers ###

"""
Certain applications require arbitrary precision arithmetic. One way to achieve this is to use arrays
to represent integers, e.g., with one digit per array entry, with the most significant digit appearing
first, and a negative leading digit denoting a negative integer. For example, (1,9,3,7,0,7,7,2,1)
represents 193707721 and (-7,6,1,8,3,8,2,5,7,2,8,7) represents -761838257287.

Write a program that takes two arrays representing integers, and returns an integer represent
ing their product. For example, since 193707721 X -761838257287 = -147573952589676412927, if
the inputs are (1,9,3,7,0,7,7,2,1) and (-7,6,1,8,3,8,2,5,7,2,8,7), your function should return
(-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7).

Hint: Use arrays to simulate the grade-school multiplication algorithm
"""

import functools
from itertools import cycle, repeat
import itertools
import math
from operator import mod
from typing import Dict, List, Tuple


"""
# >>> multiplication_table[9,3]
# 27
#
"""
multiplication_table: Dict[Tuple[int, int], int]
multiplication_table = {
    (x, y): x * y for x in range(0, 10) for y in range(0, 10)
}


def multiply_(ds1: List[int], ds2: List[int]) -> List[int]:
    """
    O(n*m)

    Takes two numbers, encoded as reverse-digit arrays, and multiplies them

    Pre-conditions:
    - |Digit| must be <= 9
    - Only the last digit (frontmost in non-reverse encoding) may be negative

    Algorithm: Sum of products like high school multiplication:
    ##################
               A  B  C
        *      X  Y  Z
        --------------
              ZA ZB ZC
            YA YB YC 0
        + XA XB XC 0 0
        --------------
                   ...
    ##################
    -

    # >>> multiply_([1,2,3], [1,2,3])
    # [1, 4, 0, 3, 0, 1]
    #
    # >>> multiply_([9,9,-9], [9,9,9])
    # [1, 0, 0, 8, 9, -9]
    #

    """
    match ds1, ds2:
        # Zeroes
        case [0], _:
            return [0]
        case _, [0]:
            return [0]
        # Product Identities
        case [], x:
            return x
        case x, []:
            return x
        case [1], x:
            return x
        case x, [1]:
            return x
        # Negative Numbers
        case x, y if x[-1] < 0 and y[-1] < 0:
            ds1[-1] = abs(ds1[-1])
            ds2[-1] = abs(ds2[-1])
            return multiply_(ds1, ds2)
        case x, y if x[-1] < 0 or y[-1] < 0:
            ds1[-1] = abs(ds1[-1])
            ds2[-1] = abs(ds2[-1])
            res = multiply_(ds1, ds2)
            res[-1] *= -1
            return res
        case _, _:
            carry: int = 0  # Value to carry over
            curr_ix: int = 0  # Product index, or what index of digit in `ds2` we're currently at
            products: List[List[int]] = []

            for d2 in ds2:
                products.append(list(repeat(0, times=curr_ix)))
                for d1 in ds1:
                    new_digit_w_carry = multiplication_table[d1, d2] + carry
                    new_digit = new_digit_w_carry % 10
                    carry = new_digit_w_carry // 10
                    products[curr_ix].append(new_digit)
                if carry:
                    products[curr_ix].append(carry)
                carry = 0
                curr_ix += 1

            final_product: List[int] = []
            for p in products:
                final_product = sum_(final_product, p)

            return final_product


def sum_(ds1: List[int], ds2: List[int], carry: int = 0) -> List[int]:
    """
    O(max(n, m)).

    # >>> sum_([1,2,3], [1,2,3])
    # [2, 4, 6]
    #
    # >>> sum_([9,9,-9], [9,9,-9])
    # [8, 9, 9, -1]
    #
    # >>> sum_([-1], [0])
    # [-1]
    #
    
    # >>> toDigitList(fromDigitList([1,-1]) + fromDigitList([0]))
    # [1, -1]
    #
    """
    match is_positive(ds1), is_positive(ds2):
        case False, False:
            ds1[-1] *= -1
            ds2[-1] *= -1
            negated = sum_(ds1, ds2)
            negated[-1] *= -1
            return negated
        case (False, True) | (True, False): # TODO Actually implement subtraction
            return toDigitList(fromDigitList(ds1) + fromDigitList(ds2))
        case True, True: 
            match ds1, ds2:
                case [], []:
                    return [] if carry == 0 else [carry]
                case ds, []:
                    return sum_(
                        [], ds, carry=carry
                    )  # No or-patterns. Flip so we don't have to implement twice
                case [], [digit, *tail]:
                    digit_with_carry: int = carry + digit
                    new_carry: int = digit_with_carry // 10
                    new_digit: int = digit_with_carry % 10
                    return [new_digit] + sum_([], tail, carry=new_carry)
                case [d1, *tail1], [d2, *tail2]:
                    digit_with_carry: int = carry + d1 + d2
                    new_carry: int = digit_with_carry // 10
                    new_digit: int = digit_with_carry % 10
                    return [new_digit] + sum_(tail1, tail2, carry=new_carry)


def is_positive(ds: List[int]) -> bool:
    """
    # >>> is_positive([9,9,-9])
    # False
    #
    # >>> is_positive([1,2,3])
    # True
    #
    """
    match ds:
        case []: return True
        case _: return ds[-1] >= 0


def toDigitList(n: int) -> List[int]:
    """
    Reverse-digit array encoding of an integer

    # >>> toDigitList(-100)
    # [0, 0, -1]
    #
    # >>> toDigitList(-11)
    # [1, -1]
    #
    """
    match abs(n):
        case x if x <= 9:
            return [x * -1] if n < 0 else [x]
        case x:
            return [x % 10] + toDigitList(x // 10 * (-1 if n < 0 else 1))


def fromDigitList(ds: List[int], place: int = 0) -> int:
    """
    From reverse-digit array encoding of an integer back to regular integer encoding

    # >>> fromDigitList([2, 9, 0, 1])
    # 1092
    #
    # >>> fromDigitList([1, -1])
    # -11
    #
    """
    match ds:
        case []:
            return 0
        case _ if ds[-1] < 0: 
            ds[-1] *= -1
            return -1 * fromDigitList(ds)
        case [digit, *tail]:
            return digit * (10**place) + fromDigitList(tail, place + 1)
