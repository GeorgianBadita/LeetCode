  # https: // leetcode.com/problems/find-all-the-lonely-nodes/

  from typing import List

   # Definition for a binary tree node.

   class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    class Solution:
        def getLonelyNodes(self, root: TreeNode) -> List[int]:
            queue = [root]
            lonely_nodes = []

            while queue:
                current_node = queue.pop(0)
                num_child = 0
                if current_node.left:
                    queue.append(current_node.left)
                    num_child += 1
                if current_node.right:
                    queue.append(current_node.right)
                    num_child += 1
                if num_child == 1:

                    lonely_nodes.append(
                        current_node.left.val if current_node.left else current_node.right.val)

            return lonely_nodes
