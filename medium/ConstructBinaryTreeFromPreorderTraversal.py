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
        if start > end:
            return TreeNode()

        if start == end or end == start + 1:
            return TreeNode(preorder[start])

        root = TreeNode(preorder[start])
        split_index = start
        for i in range(start, end):
            if preorder[i] > preorder[start]:
                split_index = i
                break
        root.left = self.build_from_preorder(preorder, start + 1, split_index)
        root.right = self.build_from_preorder(preorder, split_index + 1, end)
        return root

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.build_from_preorder(preorder, 0, len(preorder))


print(Solution().bstFromPreorder([8, 5, 1, 7, 10, 12]))
