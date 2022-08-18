### 9.1 Test if a binary tree is height-balanced ###


"""
A binary tree is said to be height-balanced if for each node in the tree, the difference in the height of
its left and right subtrees is at most one. A perfect binary tree is height-balanced, as is a complete
binary tree. A height-balanced binary tree does not have to be perfect or complete—see Figure 9.2
on the next page for an example.

Write a program that takes as input the root of a binary tree and checks whether the tree is height-
balanced.

Hint: Think of a classic binary tree algorithm.
"""

from typing import TypeVar
from ch9_binary_trees.tree_utils import TreeNode


T = TypeVar("T")


def is_height_balanced(node: TreeNode[T]) -> bool:
    """
    O(n) time + O(h) space (call stack)

    # >>> is_height_balanced(TreeNode(10, None, None))
    # True
    #

    # >>> is_height_balanced(TreeNode(10, TreeNode(10), None))
    # True

    # >>> is_height_balanced(TreeNode(10, TreeNode(10, None, TreeNode(10)), None))
    # False

    # >>> is_height_balanced(TreeNode(10, TreeNode(10, None, TreeNode(10)), TreeNode(10, TreeNode(10, TreeNode(10)))))
    # True
    """
    match node:
        case TreeNode(_, None, None):
            return True
        case TreeNode(_, child, None) | TreeNode(_, None, child):
            match child:
                case TreeNode(_, None, None):
                    return True
                case _:
                    return False
        case TreeNode(_, left, right):
            return True and is_height_balanced(left) and is_height_balanced(right)
        # case TreeNode(_, left, right):
        #     return max_depth(left) - max_depth(right) <= 1


def max_depth(node: TreeNode[T]) -> int:
    """
    O(n)

    # >>> max_depth(TreeNode(10, None, TreeNode(10, None, TreeNode(10))))
    """
    match node:
        case TreeNode(_, None, None):
            return 1
        case TreeNode(_, left, None):
            return 1 + max_depth(left)
        case TreeNode(_, None, right):
            return 1 + max_depth(right)
        case TreeNode(_, left, right):
            return 1 + max(max_depth(left), max_depth(right))
