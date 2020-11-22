# https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def get_inorder(self, root):
        stack = []
        inorder = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            cur_node = stack.pop()
            inorder.append(cur_node.val)
            root = cur_node.right
        return inorder

    def create_balaned_tree(self, inorder, start, end):
        if start > end:
            return None


        mid = (start + end) // 2
        root = TreeNode(inorder[mid])
        root.left = self.create_balaned_tree(inorder, start, mid - 1)
        root.right = self.create_balaned_tree(inorder, mid + 1, end)
        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = self.get_inorder(root)
        return self.create_balaned_tree(inorder, 0, len(inorder) - 1)

