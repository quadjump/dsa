from dataclasses import dataclass
from typing import Any, Generic, List, Optional, TypeVar

# import hypothesis.strategies as st

T = TypeVar("T")

### Singley-Linked List
# >>> Node(1, Node(2))
# Node(data=1, next_node=Node(data=2, next_node=None))
#
@dataclass
class Node(Generic[T]):
    data: T
    next: Optional["Node"] = None


# st.register_type_strategy(st.lists(st.integers()))


def reverse_linked_list(xs: Node[T]) -> Node[T]:
    """
    O(n) time, O(1) space
    """
    prev: Node[T] = None  # type: ignore
    curr: Node[T] = xs

    while curr != None:
        temp: Optional[Node[T]] = curr.next

        curr.next = prev
        prev = curr
        curr = temp

    return prev


def reverse_list_rec(curr: Node[T], prev: Optional[Node[T]] = None) -> Node[T]:
    """
    O(n) time, O(n) space

    # >>> reverse_list_rec(from_list(range(5)))
    # Node(data=4, next=Node(data=3, next=Node(data=2, next=Node(data=1, next=Node(data=0, next=None)))))
    #
    """
    match curr:
        case Node(x, None):
            return Node(x, prev)
        case node:
            return reverse_list_rec(curr=node.next, prev=Node(node.data, prev))


def from_list(xs: List[T]) -> Optional[Node[T]]:
    """
    # >>> from_list(range(5))
    # Node(data=0, next_node=Node(data=1, next_node=Node(data=2, next_node=Node(data=3, next_node=Node(data=4, next_node=None)))))
    #
    # >>> from_list([1])
    # Node(data=1, next_node=None)
    #
    """
    match xs:
        case []:
            return None
        case [x, None]:
            return Node(x, None)
        case [x, *tail]:
            return Node(x, from_list(tail))
        case _:
            raise Exception("Impossible case")


def to_list(xs: Node[T]) -> List[T]:
    """
    # >>> to_list(from_list(range(5)))
    # [0, 1, 2, 3, 4]
    #
    """
    match xs:
        case Node(x, None):
            return [x]
        case Node(x, tail):
            return [x] + to_list(tail)


def node_len(xs: Node[T]) -> int:
    """
    # >>> node_len(Node(1, Node(2, Node(3))))
    # 3
    #
    """
    match xs:
        case None:
            return 0
        case Node(_, tail):
            match tail:
                case None:
                    return 1
                case t:
                    return 1 + node_len(t)


def append(val: T, xs: Optional[Node[T]]) -> Node[T]:
    """
    O(n)

    # >>> append(3, Node(1, Node(2)))
    # Node(data=1, next_node=Node(data=2, next_node=Node(data=3, next_node=None)))
    #
    """
    match xs:
        case None:
            return Node(val)
        case Node(x, None):
            return Node(x, Node(val))
        case Node(x, next):
            return Node(x, append(val, next))


def prepend(val: T, xs: Optional[Node[T]]) -> Node[T]:
    """
    O(1)

    # >>> prepend(1, Node(2, Node(3)))
    # Node(data=1, next_node=Node(data=2, next_node=Node(data=3, next_node=None)))
    #
    """
    return Node(val, xs)


### List API ###


def search(key: T, xs: Node[T]) -> bool:
    """
    # >>> search(2, Node(1, Node(2)))
    # True
    #
    # >>> search(5, Node(1, Node(2)))
    # False
    #
    """
    match xs:
        case None:
            return False
        case Node(x, _) if x == key:
            return True
        case Node(_, tail):
            match tail:
                case None:
                    return False
                case ys:
                    return search(key, ys)
        case _:
            raise Exception("Impossible case")


# # Insert new_node after node.
# def insert_after(node, new_node):
#     """
#     # >>> x = insert_after(Node(2, Node(3)), Node(1)); x
#     # >>> x = insert_after(Node(1, Node(2)), Node(3, Node(4)))
#     """
#     new_node.next_node = node.next_node
#     node.next_node = new_node
#     return node

# # Delete the node past this one. Assume node is not a tail.
# def delete_snd(node: Node):
#     """
#     # >>> delete_snd(Node(1, Node(2, Node(3))))
#     # Node(data=1, next_node=Node(data=3, next_node=None))
#     #
#     """
#     node.next_node = node.next_node.next_node
#     return node

### Stack API ###


def push(val: T, xs: Optional[Node[T]]) -> Node[T]:
    """O(1)"""
    return prepend(val, xs)


def pop(xs: Node[T]) -> T:
    """
    O(1)

    # >>> pop(Node(1, Node(2)))
    # 1
    #
    """
    return xs.data


# # >>> Node(1, Node(2))
# # Node(data=1, next_node=Node(data=2, next_node=None))
# #
# """Doesn't really make sense since Python doesn't have pointers, so it would have to be O(n^2) space with additonal consistency logic for little benefit"""
# @dataclass
# class DoubleyNode(Generic[T]):
#     data: T
#     next_node: Optional['DoubleyNode'] = None
#     prev_node: Optional['DoubleyNode'] = None
