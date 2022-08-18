###

"""
A binary tree is symmetric if you can draw a vertical line through the root and then the left subtree
is the mirror image of the right subtree. The concept of a symmetric binary tree is illustrated in
Figure 9.3.

Symmetric Tree:
    314
   /    \
  6      6
  \      /
   2     2
    \   /
    3   3

Asymmetric Trees:
    314
   /    \
  6      6
  \      /
 561     2
    \   /
    3   1

    314
   /    \
  6      6
  \      /
   2     2
    \   /
    3   3


Write a program that checks whether a binary tree is symmetric.
Hint: The definition of symmetry is recursive.
"""

from typing import TypeVar

from ch9_binary_trees.tree_utils import TreeNode


T = TypeVar("T")


def is_symmetric(node: TreeNode[T]) -> bool:
    """
    # >>> is_symmetric(TreeNode(314, TreeNode(6), TreeNode(6)))
    """
    match node:
        case TreeNode(_, None, None):
            return True
        case TreeNode(_, _, None) | TreeNode(_, None, _):
            return False
        case TreeNode(_, left, right) if left.data == right.data:
            return is_left_right_symmetric(left, right)
        case _:
            return False


def is_left_right_symmetric(l: TreeNode[T], r: TreeNode[T]) -> bool:
    match l, r:
        case TreeNode(v1, None, None), TreeNode(v2, None, None) if v1 == v2: return True
        case TreeNode(v1, l1, None), TreeNode(v2, None, r2) if v1 == v2: return is_left_right_symmetric(l1, r2)
        case TreeNode(v1, None, r1), TreeNode(v2, l2, None) if v1 == v2: return is_left_right_symmetric(r1, l2)
        case TreeNode(v1, l1, r1), TreeNode(v2, l2, r2) if v1 == v2:
            return is_left_right_symmetric(l1, r2) and is_left_right_symmetric(r1, l2)
        case _, _: return False
