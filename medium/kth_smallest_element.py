"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   04.04.2020 22:45
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None





class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        st = []
        curr = root
        while True:
            if curr:
                st.append(curr)
                curr = curr.left
            elif st:
                curr = st.pop()
                k -= 1
                if not k:
                    return curr.val
                curr = curr.right
            else:
                break


#  3
#  / \
# 1   4
#  \
#   2

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

print(Solution().kthSmallest(root, 1))