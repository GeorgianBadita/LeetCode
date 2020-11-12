# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def is_symmetric_rec(self, root1, root2):

        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False

        return self.is_symmetric_rec(root1.left, root2.right) and self.is_symmetric_rec(root1.right, root2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_symmetric_rec(root, root)
