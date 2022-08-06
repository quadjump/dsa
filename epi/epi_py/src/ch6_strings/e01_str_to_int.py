### 6.1 Interconvert strings and integers ###

"""
A string is a sequence of characters. A string may encode an integer, e.g., "123" encodes 123. In
this problem, you are to implement methods that take a string representing an integer and return
the corresponding integer, and vice versa. Your code should handle negative integers. You cannot
use library functions like int in Python.

Implement an integer to string conversion function, and a string to integer conversison function.

For example, if the input to the first function is the integer 314, it should return the string "314" and
if the input to the second function is the string "314" it should return the integer 314.

Hint: Build the result one digit at a time.
"""

from typing import Dict


def to_int(digits: str) -> int:
    """
    # >>> to_int("-2345")
    # -2345
    #
    # >>> reversed("123")
    # <reversed object at 0x7f6f9f0cfe80>
    #
    """
    match digits:
        case "": return 0
        case neg if neg[0] == '-': return -1 * to_int(neg[1:])
        case pos: return to_int_rev(pos[::-1])

def to_int_rev(digits: str) -> int:
    """
    Reverse encoded string number to integer.

    # >>> to_int_rev("321")
    # 123
    #
    """
    match digits:
        case "":
            return 0
        case ds if len(ds) == 1:
            return to_digit(ds[0])
        case ds:
            return to_digit(ds[0]) + 10 * to_int_rev(ds[1:])


def to_digit(d: str) -> int:
    match d:
        case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
            return digit_map[d]
        case _:
            raise Exception("Not a digit")


digit_map: Dict[str, int] = {f"{i}": i for i in range(10)}
