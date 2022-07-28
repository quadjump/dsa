### 5.4 Advancing through an array ###

"""
In a particular board game, a player has to try to advance through a sequence of positions. Each
position has a nonnegative integer associated with it, representing the maximum you can advance
from that position in one move. You begin at the first position, and win by getting to the last
position. 

For example, let A = (3,3,1,0,2,0,1) represent the board game, i.e., the zth entry in A is
the maximum we can advance from i. Then the game can be won by the following sequence of
advances through A: take 1 step from A[0] to A[1], then 3 steps from A[1] to A[4], then 2 steps from
A[4] to A[6], which is the last position. Note that A[0] = 3 >= 1, A[1] = 3 >= 3, and A[4] >= 2 > 2, so all
moves are valid. If A instead was (3,2,0,0,2,0,1), it would not possible to advance past position 3,
so the game cannot be won.

Write a program which takes an array of n integers, where A[z] denotes the maximum you can
advance from index i, and returns whether it is possible to advance to the last index starting from
the beginning of the array.

Hint: Analyze each location, starting from the beginning
"""

from functools import reduce
from typing import Dict, List, Set


def can_reach_end(board: List[int]) -> bool:
    """
    O(b).

    # >>> can_reach_end([3,3,1,0,2,0,1])
    # True
    #
    # >>> can_reach_end([3,2,0,0,2,0,1])
    # False
    #
    # >>> can_reach_end([2,0,3,0,0,0,0])
    # True
    #
    # >>> can_reach_end([0])
    # True
    #

    """
    match board:
        case []:
            return True
        case [x]:
            return True
        case [0, _]:
            return False
        case [step, *rest_of_board]:
            for x in range(0, min(step, len(rest_of_board))):
                return False or can_reach_end(rest_of_board[step:])
        case _:
            raise Exception("The impossible happened")


### Variant: Minimum Moves to Win ###

"""
Write a program to compute the minimum number of steps needed to advance to the last
location.
"""


def build_advances(board: List[int]) -> List[List[int]]:
    """
    O(b^2).

    Brute force collect all valid and invalid paths

    TODO Prune invalid paths
    TODO Fuse build/fold

    # >>> build_advances([3,3,1,0,2,0,1])
    # [[1, 3, 2]]
    #
    # >>> build_advances([3,2,0,0,2,0,1])
    # []
    #
    # >>> build_advances([2,0,3,0,0,0])
    # [[2, 3]]
    #
    # >>> build_advances([0])
    # [[]]
    #

    """
    match board:
        case []:  # Valid Path
            return []
        case [x]:  # Valid Path
            return [[]]
        case [0, _]:  # Invalid Path, unable to reach end
            return []
        case [move, *rest_of_board]:
            return [
                [step + 1] + advance
                for step in range(0, min(move, len(rest_of_board)))
                for advance in build_advances(rest_of_board[step:])
            ]
        case _:
            raise Exception("Impossible case reached")


def find_optimal_advance(paths: List[List[int]]) -> List[int]:
    """
    Fold all paths to single optimal path with least number of moves
    """
    match paths:
        case []:
            return []
        case all_paths:
            return reduce(
                lambda min_path, curr_path: curr_path
                if len(curr_path) <= len(min_path)
                else min_path,
                all_paths,
            )


def advance(board: List[int]) -> List[int]:
    """
    O(b^2) (build: O(b^2), fold: O(b) assuming constant `len` call)

    Build up all possible board traversals, then reduce down to a single optimal traversal.

    # >>> advance([3,3,1,0,2,0,1])
    # [1, 3, 2]
    #

    # >>> advance([3,2,0,0,2,0,1])
    # []
    #

    # >>> advance([1,1])
    # [1]
    #
    """
    return find_optimal_advance(build_advances(board))
