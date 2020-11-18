# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        q_set = set()
        while q:
            q_set.add(q)
            q = q.parent
        
        while p:
            if p in q_set:
                return p
            p = p.parent

