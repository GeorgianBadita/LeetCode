"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   11.04.2020 21:53
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def construct(root1, root2):
    if not root1 and not root2:
        return None
    node = TreeNode(None)
    if not root1 and root2:
        node.val = root2.val
    elif root1 and not root2:
        node.val = root1.val
    elif root1 and root2:
        node.val = root2.val + root1.val

    if root1 and root2:
        node.left = construct(root1.left, root2.left)
        node.right = construct(root1.right, root2.right)
    elif root1 and not root2:
        node.left = construct(root1.left, root2)
        node.right = construct(root1.right, root2)
    elif not root1 and root2:
        node.left = construct(root1, root2.left)
        node.right = construct(root1, root2.right)
    elif not root1 and not root2:
        node.left = construct(root1, root2)
        node.right = construct(root1, root2)
    return node


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and t2:
            return t2
        if not t2 and t1:
            return t1
        if not t2 and not t1:
            return None
        return construct(t1, t2)


root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.left = TreeNode(3)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

root = Solution().mergeTrees(root1, root2)

print()