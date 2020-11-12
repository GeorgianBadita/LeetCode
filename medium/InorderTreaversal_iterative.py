# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/786/

from typing import List

    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        traversal = []
        stack = []
        while stack or root:
            
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            traversal.append(root.val)
            root = root.right
        
        return traversal
