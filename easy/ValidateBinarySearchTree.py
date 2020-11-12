# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def validate_bst(self, root, min_val, max_val):
        if not root:
            return True
        if not min_val < root.val < max_val:
            return False

        return self.validate_bst(root.left, min_val, root.val) and self.validate_bst(root.right, root.val, max_val)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate_bst(root, -10 ** 10, 10 ** 10)
