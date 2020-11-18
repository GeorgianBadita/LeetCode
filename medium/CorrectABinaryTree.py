# https://leetcode.com/problems/correct-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        vis_set = set()
        queue = [(root, None, '')]

        while queue:
            curr_node, parent, dir = queue.pop(0)
            vis_set.add(curr_node)

            if curr_node.right:
                if curr_node.right in vis_set:
                    if parent and dir == 'left':
                        parent.left = None
                    elif parent and dir == 'right':
                        parent.right = None
                    break
                queue.append((curr_node.right , curr_node, 'right'))
            if curr_node.left:
                queue.append((curr_node.left, curr_node, 'left'))

        return root
