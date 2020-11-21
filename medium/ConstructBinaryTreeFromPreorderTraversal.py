# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def build_from_preorder(self, preorder, start, end):

        if end  == start + 1:
            curr_val = preorder[start]
            next_val = preorder[start + 1]
            root = TreeNode(curr_val)
            if curr_val > next_val:
                root.left = TreeNode(next_val)
            else:
                root.right = TreeNode(next_val)
            return root

        if start > end:
            return None

        if start == end:
            return TreeNode(preorder[start])
        
        split_index = start
        for i in range(start, end + 1):
            if preorder[i] > preorder[start]:
                split_index = i
                break
        if split_index == start:
            split_index = end + 1
        root = TreeNode(preorder[start])
        root.left = self.build_from_preorder(preorder, start + 1, split_index - 1)
        root.right = self.build_from_preorder(preorder, split_index, end)
        return root

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.build_from_preorder(preorder, 0, len(preorder) - 1)



