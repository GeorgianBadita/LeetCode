"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 20:31
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


class SolutionTraversal:
    def isValidBST(self, root: TreeNode) -> bool:
        traversal = inorder_traversal(root)
        for i in range(len(traversal) - 1):
            if traversal[i] >= traversal[i + 1]:
                return False
        return True


def solve_min_max(root, min_val, max_val):
    if not root:
        return True
    if not min_val < root.val < max_val:
        return False
    return solve_min_max(root.left, min_val, root.val) and solve_min_max(root.right, root.val, max_val)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return solve_min_max(root, -2 ** 31 - 1, 2 ** 31 + 1)


root = TreeNode(-2147483648)
# root.left = TreeNode(1)
# root.right = TreeNode(3)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(6)

print(Solution().isValidBST(root))
