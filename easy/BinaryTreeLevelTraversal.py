# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        sol = []
        queue = [(root, 0)]

        while queue:
            node, level = queue.pop(0)
            if level == len(sol):
                sol.append([node.val])
            else:
                sol[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return sol
