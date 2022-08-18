### 8.3 Lowest Common Ancestor ###

"""
"""

from typing import List, NewType, TypeVar

from ch9_binary_trees.tree_utils import TreeNode


MemoryLoc = NewType("MemoryLoc", int)

T = TypeVar("T")

def lca(root: TreeNode[T], node1: MemoryLoc, node2: MemoryLoc) -> TreeNode[T]:
    def find_ancestry(tree, node) -> List[TreeNode[T]]:
        """
        DFS to node
        """
        if tree is node: return [node]
        # match tree:
        #     case Node()