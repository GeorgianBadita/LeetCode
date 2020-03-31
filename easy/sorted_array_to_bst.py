"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 20:53
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def make_balanced_rec(nums, left, right):
    if left > right:
        return None

    mid = (left + right) // 2
    curr_node = TreeNode(nums[mid])
    curr_node.left = make_balanced_rec(nums, left, mid - 1)
    curr_node.right = make_balanced_rec(nums, mid + 1, right)
    return curr_node


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return make_balanced_rec(nums, 0, len(nums) - 1)


def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val)
        print_inorder(root.right)


root = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
print_inorder(root)
