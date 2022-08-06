### 7.10 Implement even-odd merge ###

"""
Consider a singly linked list whose nodes are numbered starting at 0. Define the even-odd merge of
the list to be the list consisting of the even-numbered nodes followed by the odd-numbered nodes.

The even-odd merge is illustrated in Figure 7.10.

Write a program that computes the even-odd merge.

Hint: Use temporary additional storage.
"""

import sys
from typing import List, TypeVar
from ch7_lists.list_utils import Node, from_list, to_list


T = TypeVar('T')

def even_odd_merge_clean(xs: Node[T]) -> Node[T]:
    """
    O(n) space + time
    
    # >>> to_list(even_odd_merge_clean(from_list(range(5)))) 
    # [0, 2, 4, 1, 3]
    #
    """
    xs_: List[T] = to_list(xs)
    evens: List[T] = []
    odds: List[T] = []

    is_even: bool = True
    for ix in range(len(xs_)):
        if is_even: evens += [xs_[ix]]
        else: odds += [xs_[ix]]
        is_even = not is_even
        
    return from_list(evens + odds)


# Book Solution
def even_odd_merge(xs: Node[T]) -> Node[T]:
    """
    O(n) time, O(1) space

    # >>> to_list(even_odd_merge(from_list(range(5)))) 
    # [0, 2, 4, 1, 3]
    #

    I'm guessing there's a three pointer + sentinel strategy
    - 3 Pointers
        - Evens root
        - Odds root (end of evens)
        - Runner
    """
    match xs:
        case Node(x, None): return xs
        case Node(x, Node(y, None)): return xs
        case _:
            even_sentinel: Node[T] = Node(sys.maxsize)  # type: ignore
            odd_sentinel: Node[T] = Node(sys.maxsize)  # type: ignore
            
            tails: List[Node[T]] = [even_sentinel, odd_sentinel]  # LMAO NO SUM TYPES
            odd_flag: int = 0  # 0=False, 1=True

            while xs != None:
                tails[odd_flag].next = xs  # Append to even/odd sentinel
                xs = xs.next  # Iterate list
                tails[odd_flag] = tails[odd_flag].next  # Iterate sentinel
                odd_flag ^= 1  # Alternate between even and odd.
            
            tails[0].next = odd_sentinel.next
            tails[1].next = None
            
            return even_sentinel.next