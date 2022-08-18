### 8.2 Evaluate RPN expressions ###

"""
A string is said to be an arithmetical expression in Reverse Polish notation (RPN) if:

1. It is a single digit or a sequence of digits, prefixed with an option
e.g., "6", "123", "-42".

2. It is of the form "A, B, o" where A and B are RPN expressions and o is one of +, —, X, /.
For example, the following strings satisfy these rules: "1729", "3,4,+,2, X, 1,+", "1,1,+, —2, X",
"-641,6,/, 28,/".

An RPN expression can be evaluated uniquely to an integer, which is determined recursively.
The base case corresponds to Rule (1.), which is an integer expressed in base-10 positional system.
Rule (2. Corresponds to the recursive case, and the RPNs are evaluated in the natural way, e.g., if A
evaluates to 2 and B evaluates to 3, then "A, B, x" evaluates to 6.
Write a program that takes an arithmetical expression in RPN and returns the number that the
expression evaluates to.

Hint: Process subexpressions, keeping values in a stack. How should operators be handled?
"""

from typing import Callable, Dict, List, NewType, Optional, Tuple, Union
import operator


"""
data Operator = Add | Mult | Sub | Div

data RPN = 
    Accumulated Int
  | Pair Int Int
  | Op Operator

eval :: [RPN] -> Int
"""

# >>> ops["+"](1, 3)
# 4
#
ops: Dict[str, Callable[[int, int], int]] = {
    "+": lambda a, b: operator.add(a, b),  # type: ignore
    "*": lambda a, b: operator.mul(a, b),  # type: ignore
    "-": lambda a, b: operator.sub(a, b),  # type: ignore
    "/": lambda a, b: operator.floordiv(a, b),  # type: ignore
}


def eval_rpn_adt(tokens: List[str]) -> int:
    """
    O(n).

    # >>> eval_rpn_adt(["2", "1", "+", "3", "*"])
    # 9
    #

    # >>> list(map(eval_rpn_adt, [["1729"], ["3", "4", "+", "2", "*", "1", "+"], ["1", "1", "+", "-2", "*"], ["-641", "6", "/", "28", "/"]]))
    # [1729, 15, -4, -4]
    #
    """
    return eval_rpn_adt_(tokens=tokens[1:], acc=int(tokens[0]))


def eval_rpn_adt_(tokens: List[str], acc: Union[int, Tuple[int, int]]) -> int:
    """
    Accumulator is either an accumulated integer or a pair of integers to be combined when applying the upcoming operator.
    """
    match tokens, acc:
        case [], (x, y): raise Exception("Illegal input")
        case [], x: return x
        case [op], (x, y) if op in ops: return ops[op](x, y)
        case [op, *tail], (x, y) if op in ops: return eval_rpn_adt_(tail, acc=ops[op](x, y))
        case [num, *tail], x: return eval_rpn_adt_(tail, acc=(x, int(num)))
        case _, _: raise Exception("Invalid input bro")
