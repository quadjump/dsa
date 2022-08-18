from dataclasses import dataclass
from typing import Generic, List, NewType, Optional, TypeAlias, TypeVar


T = TypeVar("T")


@dataclass
class StackNode(Generic[T]):
    element: T
    max_: T


Stack = List[StackNode[T]]


def empty(s: Stack[T]) -> bool:
    """
    # >>> empty([])
    # True
    #
    """
    match s:
        case []:
            return True
        case _:
            return False


def push(key: T, s: Stack[T]) -> Stack[T]:
    """
    O(1)

    # >>> push(3, push(2, push(1, [])))
    # [StackNode(element=3, max_=3), StackNode(element=2, max_=2), StackNode(element=1, max_=1)]
    #
    """
    return [
        StackNode(
            element=key, max_=key if empty(s) else max(key, top(s).max_)  # type: ignore
        )
    ] + s


def pop(s: Stack[T]) -> Optional[StackNode[T]]:
    """
    O(1)

    # >>> pop(push(3, push(2, push(1, []))))
    # StackNode(element=3, max_=3)
    #
    """
    match s:
        case []:
            return None
        case [x, *_]:
            # s.max_ = max_manual(s.elements[1:])
            return x
    return None


def top(s: Stack[T]) -> StackNode[T]:
    """
    O(1)

    # >>> top(push(1, []))
    # StackNode(element=1, max_=1)
    #
    """
    return s[0]


def max_(s: Stack[T]) -> T:
    """
    O(1)
    # >>> max_(push(3, push(4, push(1, []))))
    # 4
    #
    """
    return top(s).max_


# def max_manual(xs: List[T], curr_max=None) -> Optional[T]:
#     """
#     # >>> max_(Stack([11,2,3]))
#     # 11
#     #
#     """
#     match s.elements:
#         case []:
#             return curr_max
#         case (x, tail):
#             return max_manual(tail, max(x, curr_max))
