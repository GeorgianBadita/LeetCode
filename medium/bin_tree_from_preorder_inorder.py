"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   04.04.2020 20:40
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def construct(preorder: List[int], inorder: List[int], l_p, r_p, l_i, r_i):
    if l_i > r_i:
        return None
    poz = None
    for i in range(l_i, r_i + 1):
        if inorder[i] == preorder[l_p]:
            poz = i
            break
    root = TreeNode(inorder[poz])
    root.left = construct(preorder, inorder, l_p + 1, l_p + poz - l_i, l_i, poz - 1)
    root.right = construct(preorder, inorder, l_p + poz - l_i + 1, r_p, poz + 1, r_i)
    return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return construct(preorder, inorder, 0, len(preorder) - 1, 0, len(preorder) - 1)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

haed= Solution().buildTree(preorder, inorder)

print()

