# Definition for Node.
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Solution:

    def __init__(self) -> None:
        self.__nodes = {}

    def solve(self, node):
        if not node:
            return None

        if node in self.__nodes:
            return self.__nodes[node]

        copy = NodeCopy(node.val)
        self.__nodes[node] = copy

        copy.left = self.solve(node.left)
        copy.right = self.solve(node.right)
        copy.random = self.solve(node.random)

        return copy

    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        return self.solve(root)