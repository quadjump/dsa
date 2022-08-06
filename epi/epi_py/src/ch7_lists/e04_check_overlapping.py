### 7.4 Test for Overlapping lists (given cycle-free lists) ###

"""
Given two singly linked lists there may be list nodes that are common to both. (This may not be a
bug—it may be desirable from the perspective of reducing memory footprint, as in the flyweight
pattern, or maintaining a canonical form.) For example, the lists in Figure 7.6 on the following page
overlap at Node I.

Write a program that takes two cycle-free singly linked lists, and determines if there exists a node
that is common to both lists.

Hint: Solve the simple cases first.
"""

from typing import Set, TypeVar
from ch7_lists.list_utils import Node, to_list

T = TypeVar("T")


def check_overlapping(xs: Node[T], ys: Node[T]) -> bool:
    """
    O(n) where n = len(xs) + len(ys)

    Check for pointer equality between end of both lists. 
    Since problem states there are no cycles, any overlap would be one-way (two-way would create cycle)
    Hence both lists end up in the same place.

    # >>> xs = Node(2, Node(3)); ys = Node(1, xs); check_overlapping(xs, ys)
    # True
    #

    # >>> xs = Node(2, Node(3)); ys = Node(2, Node(3)); check_overlapping(xs, ys)
    # False
    #

    # >>> xs = Node(2, Node(3)); ys = None; check_overlapping(xs, ys)
    # False
    #

    # >>> xs = Node(2, Node(3)); ys = xs; check_overlapping(xs, ys)
    # True
    #

    # >>> xs = Node(2); ys =  Node(2); check_overlapping(xs, ys)
    # False
    #

    """
    match xs, ys:
        case (None, _) | (_, None): return False
        case xs_, ys_ if xs_ is ys_: return True
        case _:
            # node_set: Set[Node[T]] = set()  # TypeError: unhashable type: 'Node'

            while xs.next != None:
                # node_set.add(xs)
                xs = xs.next
            
            while ys.next != None:
                # if node_set.__contains__(ys): return True
                
                # node_set.add(ys)
                ys = ys.next

            return xs is ys
