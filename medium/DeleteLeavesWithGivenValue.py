# https://leetcode.com/problems/delete-leaves-with-a-given-value/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __remove_leaf_nodes(self, root, target):
        if not root:
            return None
        left_child = self.__remove_leaf_nodes(root.left, target)
        right_child = self.__remove_leaf_nodes(root.right, target)

        if (
            left_child
            and not left_child.left
            and not left_child.right
            and left_child.val == target
        ):
            root.left = None

        if (
            right_child
            and not right_child.left
            and not right_child.right
            and right_child.val == target
        ):
            root.right = None
        return root

    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        root = self.__remove_leaf_nodes(root, target)
        return None if not root.left and not root.right and root.val == target else root


root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)

Solution().removeLeafNodes(root, 1)