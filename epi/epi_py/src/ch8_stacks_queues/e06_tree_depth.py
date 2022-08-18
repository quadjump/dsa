### 8.6 Compute binary tree nodes in order of increasing depth ###

"""
Binary trees are formally defined in Chapter 9. In particular, each node in a binary tree has a depth,
which is its distance from the root.

Given a binary tree, return an array consisting of the keys at the same level. Keys should appear
in the order of the corresponding nodes' depths, breaking ties from left to right. For example, you
should return <<314>, <6,6>, <271,561,2,271>, <28,0,3,1,28>, <17,401,257>, <641>> for the binary tree
in Figure 9.1 on Page 112.

Hint: First think about solving this problem with a pair of queues
"""

"""
Fig 9.1:

Depth    Tree
0        314
       /     \
1     6       6
     /\       /\
2   271 561  2 271
    /\   \    \  \
3  28 0   3    1  28
         /     /\
4      17    401 257
              \
5             641
"""

from collections import deque
from typing import Deque, List, Optional, TypeVar

from ch9_binary_trees.tree_utils import TreeNode

T = TypeVar("T")


def t(x: T, left=None, right=None) -> TreeNode[T]:
    return TreeNode(x, left, right)


fig9_1: TreeNode[int] = t(
    314,
    (t(6, t(271, t(28), t(0)), t(561, None, t(3, t(17), None)))),
    (t(6, t(2, None, t(1, t(401, None, t(641)), t(257))), t(271, None, t(28)))),
)


def binary_tree_depth_order(node: TreeNode[T]) -> List[List[T]]:
    """
    O(n) level-order (BFS) traversal

    # >>> binary_tree_depth_order(fig9_1)
    [[314], [6, 6], [271, 561, 2, 271], [28, 0, 3, 1, 28], [17, 401, 257], [641]]
    """
    result: List[List[T]] = []

    if node == None:
        return result

    # Collect (next level) children of current nodes (current level)
    curr_depth_nodes = [node]
    while curr_depth_nodes != []:
        result.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = [
            child
            for curr in curr_depth_nodes
            for child in (curr.left, curr.right)
            if child != None
        ]
    return result


def binary_tree_depth_queue(node: TreeNode[T]) -> List[List[T]]:
    """
    O(n) level-order (BFS) traversal with explicit python `deque`.

    # >>> binary_tree_depth_queue(fig9_1)
    [[314], [6, 6], [271, 561, 2, 271], [28, 0, 3, 1, 28], [17, 401, 257], [641]]
    """
    result: List[List[T]] = []

    if node == None:
        return result

    # Collect (next level) children of current nodes (current level)
    curr_level_queue: Deque = deque([node])
    level: int = 0
    while len(curr_level_queue) != 0:
        for _ in range(len(curr_level_queue)):
            curr = curr_level_queue.popleft()
            if curr.left != None:
                curr_level_queue.append(curr.left)
            if curr.right != None:
                curr_level_queue.append(curr.right)
            
            if level + 1 <= len(result):
                result[level] += [curr.data]
            else:
                result.append([curr.data])
        level += 1
    return result


# def level_order(node: TreeNode[T], prev_level: Optional[List[TreeNode[T]]]=None) -> List[List[T]]:
#     match node:
#         case TreeNode(val, left, right):
#             match left, right:
#                 case None, None: return [val]
#                 case None, _: return [val] + level_order(node.right) 
#                 case _, None: return [val] + level_order(node.left)
#                 case _, _: return [val] + level_order

# """
# # >>> tree_depth(fig9_1)
# """
# def tree_depth(node: TreeNode[T]) -> List[List[T]]:
#     # q: Deque = deque([])
#     node_list: List[T] = []
#     if node != None:
#         node_list.append(node.data)
#         node_list.append(tree_depth(node.left))
#         node_list.append(tree_depth(node.right))
#     return node_list


# def flatten(xss: List[List[T]]) -> List[List[T]]:
#     match xss:
#         case []: return []
#         case [xs] if isinstance(xs, T):
#             match xs:
#                 case []: return []
#                 case [x]: return []
#                 case [x, tail]: return []
#         case [xs, *tails]:
#             match xs:
#                 case []: return []
#                 case [x]: return []
#                 case [x, tail]: return []
