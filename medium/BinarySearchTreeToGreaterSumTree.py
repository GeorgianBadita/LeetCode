# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.__sum = 0

    def solve(self, root):
        if not root:
            return 0
        
        self.solve(root.right)
        root.val += self.__sum
        self.__sum = root.val
        self.solve(root.left)


    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.solve(root)
        return root
