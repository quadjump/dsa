### 7.1 Merge two sorted lists ###

"""
Consider two singly linked lists in which each node holds a number. Assume the lists are sorted,
i.e., numbers in the lists appear in ascending order within each list. The merge of the two lists is a
list consisting of the nodes of the two lists in which numbers appear in ascending order. Merge is
illustrated in Figure 7.3

Write a program that takes two lists, assumed to be sorted, and returns their merge. The only field
your program can change in a node is its next field.

Hint: Two sorted arrays can be merged using two indices. For lists, take care when one iterator reaches the
end.
"""

from typing import TypeVar
from ch7_lists.list_utils import Node, from_list

T = TypeVar('T')



def merge(xs: Node[T], ys: Node[T]) -> Node[T]:
    """
    Post-Conditions:
        - `len(merge(xs, ys)) == len(xs) + len(ys)`
    
    # >>> from_list([x for x in range(5) if x % 2 == True]), from_list([x for x in range(5) if x % 2 == False])
    # (Node(data=1, next_node=Node(data=3, next_node=None)), Node(data=0, next_node=Node(data=2, next_node=Node(data=4, next_node=None))))
    #

    # >>> merge(from_list([x for x in range(5) if x % 2 == True]), from_list([x for x in range(5) if x % 2 == False]))  
    # Node(data=0, next_node=Node(data=1, next_node=Node(data=2, next_node=Node(data=3, next_node=Node(data=4, next_node=None)))))
    #
    """
    match xs, ys:
        case None, _: return ys
        case _, None: return xs
        case Node(x, _), Node(y, ny) if x >= y: return Node(y, merge(xs, ny))
        case Node(x, nx), Node(y, _) if x < y: return Node(x, merge(nx, ys))
        case _, _: raise Exception("Impossible case")
