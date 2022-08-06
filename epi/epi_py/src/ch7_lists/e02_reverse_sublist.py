### 7.2 Reverse a single sublist ###

"""
This problem is concerned with reversing a sublist within a list. See Figure 7.4 for an example of
sublist reversal.

Write a program which takes a singly linked list L and two integers s and f as arguments, and
reverses the order of the nodes from the sth node to /th node, inclusive. The numbering begins at
1, i.e., the head node is the first node. Do not allocate additional nodes.

Hint: Focus on the successor fields which have to be updated.
"""

import sys
from typing import TypeVar
from ch7_lists.list_utils import Node, from_list, to_list

T = TypeVar("T")


def rev_sub_list(xs: Node[T], start: int, end: int) -> Node[T]:
    """
    O(n), multiple passes

    # >>> rev_sub_list(from_list(range(8)), 2, 4)
    # Node(data=0, next_node=Node(data=1, next_node=Node(data=4, next_node=Node(data=3, next_node=Node(data=2, next_node=Node(data=5, next_node=Node(data=6, next_node=Node(data=7, next_node=None))))))))
    #
    """
    res = to_list(xs)

    while start < end:
        res[start], res[end] = res[end], res[start]
        start += 1
        end -= 1

    return from_list(res)


# Book Solution
def reverse_sublist(xs: Node[T], start: int, finish: int) -> Node[T]:
    """
    O(n), single pass (trade constant factor for fucking everything else)

    Techniques:
    - Uses "dummy head"/"sentinel" to maintain reference to root of list while mutating said list
    - Uses 3 pointers (head, iterator, next) to reverse sublist
        - Maintain reference to head of sublist
        - Iterate from front to back of sublist
            - Runner for iterate through sublist advances one position
            - Extract temp node from one spot ahead of runner
                - Make temp node point to runner
                - Move temp node to front of sublist

    Reverse using "fast-and-slow pointers" from beginning of sublist

    # >>> to_list(reverse_sublist(from_list(range(8)), 2, 6))
    # [0, 1, 6, 5, 4, 3, 2, 7]
    #

    # >>> to_list(reverse_sublist(from_list(range(10)), 0, 9))
    # [0, 0]
    #
    """
    # Dummy Head/throwaway value to maintain root reference while mutating list
    sentinel: Node[T] = Node(sys.maxsize, xs)  # type: ignore

    # Get node pointing to first node in sublist
    sublist_head: Node[T] = Node(sys.maxsize, xs)  # type: ignore
    for _ in range(start):
        sublist_head = sublist_head.next  # type: ignore

    # Iteratively extract elements and move them in front of sublist
    sublist_runner: Node[T] = sublist_head.next  # type: ignore
    for _ in range(finish - start):
        # Temp node to be extracted an prepended to front of sublist
        temp: Node[T] = sublist_runner.next  # type: ignore

        sublist_runner.next = (
            temp.next
        )  # Detach temp node, making runner point beyond it
        temp.next = (
            sublist_head.next
        )  # Make detached node point to front of sublist
        sublist_head.next = temp  # Reattach node at front of sublist

    return sentinel.next  # type: ignore


def snoc(val: T, xs: Node[T]) -> Node[T]:
    """
    # >>> snoc(100, from_list(range(2)))
    # Node(data=0, next_node=Node(data=1, next_node=Node(data=100, next_node=None)))
    #
    """
    match xs:
        case None:
            return Node(val, None)
        case Node(x, None):
            return Node(x, Node(val))
        case Node(x, tail):
            return Node(x, snoc(val, tail))


def cons(val: T, xs: Node[T]) -> Node[T]:
    """
    # >>> cons(100, from_list(range(2)))
    # Node(data=100, next_node=Node(data=0, next_node=Node(data=1, next_node=None)))
    #
    """
    return Node(val, xs)


# def move_back(ix: int, dist: int, xs: Node[T]) -> Node[T]:
#     """
#     # >>> move_back(1, 2, from(list(range(5)))
#     """
#     case xs:
#         case None: return Node(val, None)
#         case Node(x, None): return Node(x, Node(val))
#         case Node(x, tail): return Node(x, snoc(val, tail))


# def rev_sub_list(xs: Node[T], start: int, end: int) -> Node:
#     """
#     # >>> rev_sub_list(from_list(range(8)), 2, 4)
#     # Node(data=0, next_node=Node(data=1, next_node=Node(data=4, next_node=Node(data=5, next_node=Node(data=6, next_node=Node(data=7, next_node=Node(data=3, next_node=Node(data=2, next_node=None))))))))
#     #
#     """
#     if start > end: raise Exception("Illegal input, start greater than end.")
#     if end == 0: return xs

#     match xs:
#         case Node(x, None): return Node(x, None)
#         # Snoc sub-list
#         case Node(x, tail) if start == 0 and end != 0: return snoc(x, rev_sub_list(tail, start, end-1))
#         # Cons remainder
#         case Node(x, tail): return cons(x, rev_sub_list(tail, start-1, end-1))

#     return Node(1, None)

## Can't build snoc-list in middle and add back in without changing return type
# def rev_sub_list(xs: Node, start: int, end: int) -> Node:
#     """
#     # >>> rev_sub_list(from_list(range(5)), 2, 4)
#     # Node(data=1, next_node=None)
#     #
#     """
#     if start > end: raise Exception("Illegal input, start greater than end.")
#     if end == 0: return xs

#     match xs:
#         case Node(x, None): return Node(x, None)
#         # Snoc sub-list
#         case Node(x, tail) if start == 0: return rev_sub_list(x, start-1, end-1)
#         # Cons remainder
#         case Node(x, tail): return Node(x, rev_sub_list(tail, start-1, end-1))


#     return Node(1, None)
