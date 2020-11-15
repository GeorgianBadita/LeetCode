# https://leetcode.com/problems/find-root-of-n-ary-tree/


from typing import List

# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        if not tree:
            return tree

        xor_sum = 0
        for node in tree:
            xor_sum ^= node.val
            for child in node.children:
                xor_sum ^= child.val
        
        for node in tree:
            if node.val == xor_sum:
                return node
