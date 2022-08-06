import sys
from typing import TypeVar
from unittest.mock import sentinel
from ch7_lists.list_utils import Node, from_list, to_list

T = TypeVar('T')

def remove_node(node_to_delete: Node[T]) -> None:
    """
    # >>> xs = from_list(range(4)); bye_node = xs.next_node; remove_node(bye_node); xs
    # Node(data=0, next_node=Node(data=1, next_node=Node(data=3, next_node=None)))
    #
    """
    node_to_delete.data = node_to_delete.next.data
    node_to_delete.next = node_to_delete.next.next


def remove_node_at(ix: int, xs: Node[T]) -> Node[T]:
    """
    # >>> remove_node_at(1, Node(99))
    # Node(data=99, next_node=None)
    #

    # >>> remove_node_at(2, from_list(range(5)))
    # Node(data=0, next_node=Node(data=1, next_node=Node(data=3, next_node=Node(data=4, next_node=None))))
    #
    """
    match xs:
        case Node(x, None): raise Exception("Illegal tail node. Problem says will not be given tail node")
        case _:
            runner: Node[T] = xs  # starts at head of list
            for _ in range(ix-1):
                if runner.next != None: runner = runner.next

            if runner.next == None:
                raise Exception("Illegal tail node. Problem says will not be given tail node") 
            
            # Delete node by pointing beyond it
            runner.next = runner.next.next
            return xs
