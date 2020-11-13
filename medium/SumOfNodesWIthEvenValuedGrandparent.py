# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        sum_curr = 0
        if root.val % 2 == 0:
            if root.left and root.left.left:
                sum_curr += root.left.left.val

            if root.left and root.left.right:
                sum_curr += root.left.right.val

            if root.right and root.right.left:
                sum_curr += root.right.left.val

            if root.right and root.right.right:
                sum_curr += root.right.right.val

        return sum_curr + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)
