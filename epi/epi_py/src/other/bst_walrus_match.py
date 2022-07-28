# https://leetcode.com/problems/search-in-a-binary-search-tree/discuss/1944560/python310-using-structural-pattern-matching-and-the-walrus-operator

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(elements: List[int]) -> Optional[TreeNode]:
    return None  # STUB


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    # >>> searchBST(TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(5, TreeNode(4), TreeNode(9))), 9).val
    # 9
    # >>> searchBST(TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(5, TreeNode(4), TreeNode(9))), 2).val
    # 2
    #
    # >>> searchBST(TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(5, TreeNode(4), TreeNode(9))), 7) == None
    # True
    #
    """
    match root:
        case TreeNode(val=v) if v == val:
            return root
        case TreeNode(left=left) if (left_search := searchBST(left, val)):
            return left_search
        case TreeNode(right=right) if (right_search := searchBST(right, val)):
            return right_search
        case _:
            return None
