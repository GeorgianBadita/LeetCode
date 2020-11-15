# https://leetcode.com/problems/maximum-binary-tree/


from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def construct_maximum(self, nums, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(nums[start])

        poz = start
        for i in range(start + 1, end + 1):
            if nums[i] > nums[poz]:
                poz = i

        root = TreeNode(nums[poz])
        root.left = self.construct_maximum(nums, start, poz - 1)
        root.right = self.construct_maximum(nums, poz + 1, end)
        return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        return self.construct_maximum(nums, 0, len(nums) - 1)


Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
