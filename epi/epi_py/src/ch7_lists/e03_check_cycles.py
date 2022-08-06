### 7.3 Test for cyclicity ###

"""
Although a linked list is supposed to be a sequence of nodes ending in null, it is possible to create
a cycle in a linked list by making the next field of an element reference to one of the earlier nodes.

Write a program that takes the head of a singly linked list and returns null if there does not exist a
cycle, and the node at the start of the cycle, if a cycle is present. (You do not know the length of the
list in advance.)

Hint: Consider using two iterators, one fast and one slow.
"""

from typing import Optional, Type, TypeVar
from ch7_lists.list_utils import Node, to_list, from_list

T = TypeVar('T')

def check_cycles_naive(xs: Node[T]) -> Optional[Node[T]]:
    """
    O(n^2) time, O(1) space

    # >>> check_cycles_naive(from_list(range(10))) 
    # False
    #
    # >>> check_cycles_naive(Node(7, from_list(range(10))))
    # True
    #
    """
    match xs:
        case Node(x, None): return None
        case Node(x, Node(y, None)): return None
        case _:
            slow: Optional[Node] = xs
            fast: Optional[Node] = slow.next  # type: ignore
            # ^Above match/case ensures existence

            while slow.next != None:
                while fast.next != None:
                    if slow is fast: return slow
                    fast = fast.next
                slow = slow.next
            
            return None


def check_cycles(xs: Node[T]) -> Optional[Node[T]]:
    """
    O(n) time, O(1) space

    # >>> check_cycles_naive(from_list(range(10))) 
    # False
    #
    # >>> check_cycles_naive(Node(7, from_list(range(10))))
    # True
    #
    """
    match xs:
        case Node(x, None): return None
        case Node(x, Node(y, None)): return None
        case _:
            slow: Optional[Node] = xs
            fast: Optional[Node] = slow.next  # type: ignore
            # ^Above match/case ensures existence

            while fast != None:
                slow = slow.next
                fast = fast.next.next

                if slow is fast: return slow
            
            return None


# ---------------------------------------------------------------------------------

def check_dups_naive(xs: Node[T]) -> bool:
    """
    O(n) time + space

    Turn to list, dedup, check change in length (or use short-circuiting method for less iterations)
    
    # >>> check_cycles_naive(from_list(range(10))) 
    # False
    #
    # >>> check_cycles_naive(Node(9, from_list(range(10))))
    # True
    #
    """
    node_list = to_list(xs)

    return len(node_list) != len(set(node_list))


def check_dups(xs: Node[T]) -> bool:
    """
    O(n^2) time, O(1) space

    # >>> check_cycles_naive(from_list(range(10))) 
    # False
    #
    # >>> check_cycles_naive(Node(7, from_list(range(10))))
    # True
    #
    """
    match xs:
        case Node(x, None): return False
        case Node(x, Node(y, None)): return x == y
        case _:
            slow: Optional[Node] = xs
            fast: Optional[Node] = slow.next  # type: ignore
            # ^Above match/case ensures existence

            while slow.next != None:
                while fast.next != None:
                    if slow.data == fast.data: return True
                    fast = fast.next
                slow = slow.next
            
            return False
