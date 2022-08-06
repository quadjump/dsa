from typing import Optional, TypeVar
from unittest.mock import sentinel
from ch7_lists.list_utils import Node, from_list, to_list

T = TypeVar("T")


def remove_node_at(ix: int, xs: Node[T]) -> Optional[Node[T]]:
    """
    # >>> remove_node_at(0, Node(99))
    # No value
    #

    # >>> remove_node_at(2, from_list(range(5)))
    # Node(data=0, next_node=Node(data=1, next_node=Node(data=3, next_node=Node(data=4, next_node=None))))
    #

    # >>> remove_node_at(6, from_list(range(5)))
    # Index out of bounds
    # Node(data=0, next_node=Node(data=1, next_node=Node(data=2, next_node=Node(data=3, next_node=Node(data=4, next_node=None)))))
    #
    """
    match xs:
        case Node(x, None):
            if ix != 0: 
                print("Index out of bounds")
            else: print("Empty")
        case _:
            runner: Node[T] = xs  # starts at head of list
            for _ in range(ix - 1):
                if runner.next != None:
                    runner = runner.next
                
                else:
                    try: runner.next.next_node.next_node
                    except: 
                        print("Index out of bounds")
                        return xs

            # Delete node by pointing beyond it
            runner.next = runner.next.next
            return xs
