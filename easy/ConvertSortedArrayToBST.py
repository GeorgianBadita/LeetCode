# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def construct_bst(self, arr, left, right):
        if right < left:
            return None

        mid_index = (left + right) // 2

        root = TreeNode(arr[mid_index])
        root.left = self.construct_bst(arr, left, mid_index - 1)
        root.right = self.construct_bst(arr, mid_index + 1, right)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.construct_bst(nums, 0, len(nums) - 1)
