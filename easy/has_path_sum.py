"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   11.04.2020 23:05
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def helper(self, root, sum):
        if root is None:
            return False
        if not root.left and not root.right and sum - root.val == 0:
            return True

        return self.helper(root.left, sum - root.val) or self.helper(root.right, sum - root.val)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        return self.helper(root, sum)


root = TreeNode(1)
root.left = TreeNode(2)

root = Solution().hasPathSum(root, 3)

print(root)