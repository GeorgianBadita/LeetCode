"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 20:15
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionIter:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        root_dept = 1
        max_depth = 1
        queue = [(root, root_dept)]
        while len(queue) != 0:
            curr_root, curr_depth = queue[0]
            queue.pop(0)
            if curr_depth > max_depth:
                max_depth = curr_depth
            if curr_root.left:
                queue.append((curr_root.left, curr_depth + 1))
            if curr_root.right:
                queue.append((curr_root.right, curr_depth + 1))
        return max_depth


class SolutionRec:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(SolutionRec().maxDepth(root))
