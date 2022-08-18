from dataclasses import dataclass
from typing import Generic, List, Optional, TypeVar


T = TypeVar("T")


@dataclass
class TreeNode(Generic[T]):
    data: T
    left: Optional["TreeNode[T]"]=None
    right: Optional["TreeNode[T]"]=None


def tree_traversal(root):
    if root != None:
        # Preorder: Processes the root before the traversals of left and right
        # children.
        print(f"Preorder: {root.data}")
        tree_traversal(root.left)
        # Inorder: Processes the root after the traversal of left child and
        # before the traversal of right child.
        print(f"Inorder: {root.data}")
        tree_traversal(root.right)
        # Postorder; Processes the root after the traversals of left and right
        # children.
        print(f"Postorder: {root.data}")


def preorder(root: TreeNode[T]) -> List[T]:
    node_list: List[T] = []
    if root != None:
        node_list.append(root.data)
        node_list.extend(preorder(root.left))
        node_list.extend(preorder(root.right))
    return node_list


def inorder(root: TreeNode[T]) -> List[T]:
    node_list: List[T] = []
    if root != None:
        node_list.extend(inorder(root.left))
        node_list.append(root.data)
        node_list.extend(inorder(root.right))
    return node_list


def postorder(root: TreeNode[T]) -> List[T]:
    node_list: List[T] = []
    if root != None:
        node_list.extend(postorder(root.left))
        node_list.extend(postorder(root.right))
        node_list.append(root.data)
    return node_list
