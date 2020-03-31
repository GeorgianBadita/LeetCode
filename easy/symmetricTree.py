"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 21:24
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymm(root1, root2):
    if not root1 and root2:
        return False
    if not root2 and root1:
        return False
    if not root1 and not root2:
        return True
    return root1.val == root2.val and isSymm(root1.left, root2.right) and isSymm(root1.right, root2.left)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return isSymm(root, root)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.right = TreeNode(2)
root.right.right = TreeNode(3)

print(Solution().isSymmetric(root))
