"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   12.04.2020 01:11
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        roots = []

        def dfs(root, is_new_tree):
            if not root:
                return False

            is_deleted = root.val in to_delete
            if is_new_tree and not is_deleted:
                roots.append(root)

            if dfs(root.left, is_deleted):
                root.left = None
            if dfs(root.right, is_deleted):
                root.right = None

            return root.val in to_delete

        dfs(root, True)
        return roots


# [1,2,null,4,3]
# [2,3]

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)

to_delete = [2, 3]

lst = Solution().delNodes(root, to_delete)

print()
