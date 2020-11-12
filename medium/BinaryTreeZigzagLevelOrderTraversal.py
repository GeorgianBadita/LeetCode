# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/787/

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        sol = []
        current_level = 0
        inverted = False
        queue = [(root, current_level)]
        while queue:
            if not inverted and queue[0][1] != current_level:
                inverted = not inverted
            elif inverted and queue[-1][1] != current_level:
                inverted = not inverted

            if not inverted:
                curr_node, current_level = queue.pop(0)

                if curr_node.left:
                    queue.append((curr_node.left, current_level + 1))
                if curr_node.right:
                    queue.append((curr_node.right, current_level + 1))
            else:
                curr_node, current_level = queue.pop()

                if curr_node.right:
                    queue.insert(0, (curr_node.right, current_level + 1))
                if curr_node.left:
                    queue.insert(0, (curr_node.left, current_level + 1))

            if current_level == len(sol):
                sol.append([curr_node.val])
            else:
                sol[current_level].append(curr_node.val)

        return sol


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
print(Solution().zigzagLevelOrder(root))
