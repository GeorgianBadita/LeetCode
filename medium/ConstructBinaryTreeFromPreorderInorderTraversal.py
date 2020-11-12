# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/788/

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.indexes = {}

    def build(self, preorder, pre_start, inorder, in_start, in_end):
        if in_start > in_end:
            return None
        
        if in_start == in_end:
            return TreeNode(inorder[in_end])
        
        root_val = preorder[pre_start]
        inorder_index = self.indexes[root_val]

        root = TreeNode(root_val)
        left_cnt = inorder_index - in_start

        root.left = self.build(preorder, pre_start + 1, inorder, in_start, inorder_index - 1)
        root.right = self.build(preorder, pre_start + left_cnt + 1, inorder, inorder_index + 1, in_end)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        self.indexes = {inorder[i]: i for i in range(len(inorder))}
        return self.build(preorder, 0, inorder, 0, len(inorder) - 1)
