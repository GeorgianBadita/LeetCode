# https://leetcode.com/problems/deepest-leaves-sum/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def find_max_level(self, root):
        if not root:
            return 0
        return 1 + max(self.find_max_level(root.left), self.find_max_level(root.right))

    def get_sum_on_level(self, root, k):
        if not root:
            return 0
        
        if k == 1:
            return root.val
        return self.get_sum_on_level(root.left, k - 1)  + self.get_sum_on_level(root.right, k - 1)

    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.get_sum_on_level(root, self.find_max_level(root))
