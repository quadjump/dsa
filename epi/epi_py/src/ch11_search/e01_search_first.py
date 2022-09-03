### 11.1 Search a sorted array for first occurrence of k ###

"""
Binary search commonly asks for the index of any element of a sorted array that is equal to a
specified element. The following problem has a slight twist on this.

[-14, -10, 2, 108, 108, 243, 285, 285, 285, 401 ]

Figure 11.1: A sorted array with repeated elements.

Write a method that takes a sorted array and a key and returns the index of the first occurrence of
that key in the array. Return -1 if the key does not appear in the array. For example, when applied
to the array in Figure 11.1 your algorithm should return 3 if the given key is 108; if it is 285, your
algorithm should return 6.

Hint: What happens when every entry equals k? Don't stop when you first see k
"""

import bisect
from typing import List


def bsearch_fst(xs: List[int], k: int) -> int:
    """
    If `k` exists in list, returns index of first occurrence.

    Otherwise returns -1.

    # >>> bsearch_fst([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 108)
    # 3
    #

    # >>> bsearch_fst([1], 1)
    # 0
    #
    """
    match xs:
        case []: return -1
        case _:
            ix = bisect.bisect_left(xs, k)
            if 0 <= ix < len(xs) and xs[ix] == k: return ix
            else: return -1

