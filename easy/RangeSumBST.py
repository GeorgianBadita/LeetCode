# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0

        if low <= root.val <= high:
            return self.rangeSumBST(root.left, low, high) + root.val + self.rangeSumBST(root.right, low, high)
        elif low <= root.val:
            return self.rangeSumBST(root.left, low, high)
        else:
            return self.rangeSumBST(root.right, low, high)
