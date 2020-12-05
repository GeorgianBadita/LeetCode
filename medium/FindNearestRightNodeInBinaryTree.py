# https://leetcode.com/submissions/detail/427464241/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        right_dict = {root: None}
        queue = [(root, None)]

        while queue:
            node, parent = queue.pop(0)
            right_dict[node] = None

            if parent:
                if parent.right and parent.right != node:
                    right_dict[node] = parent.right
                elif right_dict[parent]:
                    curr_parent = right_dict[parent]
                    while curr_parent:
                        if curr_parent.left:
                            right_dict[node] = curr_parent.left
                            break
                        elif curr_parent.right:
                            right_dict[node] = curr_parent.right
                            break
                        curr_parent = right_dict[curr_parent]
            if node == u:
                return right_dict[node]
            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))
