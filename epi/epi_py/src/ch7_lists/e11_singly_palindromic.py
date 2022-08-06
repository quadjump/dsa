### 7.11 Test whether a singly linked list is palindromic ###

"""
It is straightforward to check whether the sequence stored in an array is a palindrome. However,
if this sequence is stored as a singly linked list, the problem of detecting palindromicity becomes
more challenging. See Figure 7.1 on Page 82 for an example of a palindromic singly linked list.
Write a program that tests whether a singly linked list is palindromic.
Hint: It's easy if you can traverse the list forwards and backwards simultaneously.
"""

from typing import Optional, TypeVar

from ch7_lists.list_utils import Node, reverse_linked_list, from_list


T = TypeVar('T')

def is_palindromic(xs: Node[T]) -> bool:
    """
    # [ 1 2 3 4 5 6 ]
    #   s f
    #     s   f
    #       s     f

    # >>> is_palindromic(from_list([1,2,1]))
    # True
    #

    # >>> is_palindromic(from_list([1,2,2,1]))
    # True
    #

    # >>> is_palindromic(from_list([1,2,1,1]))
    # False
    #

    # >>> is_palindromic(from_list([1,1,1]))
    # True
    #

    """
    slow: Node[T] = xs
    fast: Node[T] = xs

    # Move `slow` to midpoint node
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next   

    first_half: Optional[Node[T]] = xs
    second_half: Optional[Node[T]] = reverse_linked_list(slow)

    # If odd number of elements, first_half will also see as it traverses original list
    while first_half != None and second_half != None:
        if first_half.data != second_half.data: return False  # type: ignore
        first_half = first_half.next  # type: ignore
        second_half = second_half.next  # type: ignore
    
    return True