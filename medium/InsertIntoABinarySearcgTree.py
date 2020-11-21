# https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        root_cpy = root
        while root_cpy:
            if val > root_cpy.val:
                if root_cpy.right is None:
                    root_cpy.right = TreeNode(val)
                    return root
                root_cpy = root_cpy.right
            else:
                if root_cpy.left is None:
                    root_cpy.left = TreeNode(val)
                    return root
                root_cpy = root_cpy.left
        
        return TreeNode(val)
