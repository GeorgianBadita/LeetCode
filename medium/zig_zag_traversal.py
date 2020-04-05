"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   04.04.2020 20:17
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        nodes_per_level = []
        queue = [(root, 0)]
        policy = 0
        curr_level = 0
        while len(queue) > 0:
            if policy == 0:
                current, lvl = queue[0]
                if lvl != curr_level:
                    curr_level = lvl
                    policy = 1
                    continue
                queue.pop(0)
                if curr_level >= len(nodes_per_level):
                    nodes_per_level.append([current.val])
                else:
                    nodes_per_level[curr_level].append(current.val)
                if current.left:
                    queue.append((current.left, curr_level + 1))
                if current.right:
                    queue.append((current.right, curr_level + 1))
            elif policy == 1:
                current, lvl = queue[-1]
                if lvl != curr_level:
                    curr_level = lvl
                    policy = 0
                    continue
                queue.pop()
                if curr_level >= len(nodes_per_level):
                    nodes_per_level.append([current.val])
                else:
                    nodes_per_level[curr_level].append(current.val)
                if current.right:
                    queue.insert(0, (current.right, curr_level + 1))
                if current.left:
                    queue.insert(0, (current.left, curr_level + 1))
        return nodes_per_level


#   3
#  / \
# 9  20
#   /  \
#  15   7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().zigzagLevelOrder(root))