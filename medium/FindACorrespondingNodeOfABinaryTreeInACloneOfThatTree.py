# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def find_node_coors_in_original(self, root, target):
        node_level_v = -1
        node_level_h = -1
        queue = [(root, 0)]

        while queue:
            node, level = queue.pop(0)
            if level != node_level_v:
                node_level_v = level
                node_level_h = 0
            else:
                node_level_h += 1
            if node == target:
                return node_level_v, node_level_h
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        node_level_v, node_level_h = self.find_node_coors_in_original(
            original, target)
        v_level_match = -1
        h_level_match = -1

        queue = [(cloned, 0)]
        while queue:
            node, level = queue.pop(0)
            if level != v_level_match:
                v_level_match = level
                h_level_match = 0
            else:
                h_level_match += 1

            if node.val == target.val and v_level_match == node_level_v and h_level_match == node_level_h:
                return node
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
