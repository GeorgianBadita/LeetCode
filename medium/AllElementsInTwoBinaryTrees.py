# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def get_inorder(self, root):
        if not root:
            return []

        return self.get_inorder(root.left) + [root.val] + self.get_inorder(root.right)

    def merge(self, list1, list2):
        res_list = [0]*(len(list1) + len(list2))
        i = 0
        j = 0
        c = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                res_list[c] = list1[i]
                i += 1
            else:
                res_list[c] = list2[j]
                j += 1
            c += 1

        while i < len(list1):
            res_list[c] = list1[i]
            i += 1
            c += 1

        while j < len(list2):
            res_list[c] = list2[j]
            j += 1
            c += 1

        return res_list

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        return self.merge(self.get_inorder(root1), self.get_inorder(root2))
