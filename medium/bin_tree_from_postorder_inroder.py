"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   05.04.2020 17:08
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        def make_tree(left_inorder, right_inorder, left_postorder, right_postorder):
            if left_inorder > right_inorder:
                return None
            if right_inorder == left_inorder:
                return TreeNode(inorder[left_inorder])

            largest = postorder[right_postorder]
            head = TreeNode(largest)
            index = inorder.index(largest, left_inorder, right_inorder + 1)

            head.left = make_tree(left_inorder, index - 1, left_postorder,
                                  left_postorder + index - left_inorder - 1)
            head.right = make_tree(index + 1, right_inorder, left_postorder + index - left_inorder,
                                   right_postorder - 1)

            return head

        right_index = len(inorder) - 1
        return make_tree(0, right_index, 0, right_index)


inorder = [1, 2, 3, 4]
postorder = [3, 2, 4, 1]
head = Solution().buildTree(inorder, postorder)
st = [head]
while len(st) > 0:
    curr = st.pop()
    print(curr.val)
    if curr.left:
        st.append(curr.left)
    if curr.right:
        st.append(curr.right)
