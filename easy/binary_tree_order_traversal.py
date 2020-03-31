"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 20:43
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        traversal = [[]]
        queue = [(root, 1)]
        while len(queue) != 0:
            curr_root, level = queue[0]
            queue.pop(0)
            if level <= len(traversal):
                traversal[level - 1].append(curr_root.val)
            else:
                traversal.append([curr_root.val])
            if curr_root.left:
                queue.append((curr_root.left, level + 1))
            if curr_root.right:
                queue.append((curr_root.right, level + 1))
        return traversal


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().levelOrder(root))
