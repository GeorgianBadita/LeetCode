# https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/

# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_inorder_traversal(self, root):
        if not root:
            return []

        return self.get_inorder_traversal(root.left) + [root.val] + self.get_inorder_traversal(root.right)

    def get_var_count(self, expr):
        count = {}
        for elem in expr:
            if elem not in count:
                count[elem] = 1
            else:
                count[elem] += 1
        return count

    def equal_expressions(self, expr1, expr2):
        expr1 = ''.join(expr1).replace('(', '').replace(')', '')
        expr2 = ''.join(expr2).replace('(', '').replace(')', '')

        return self.get_var_count(expr1) == self.get_var_count(expr2)

    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        return self.equal_expressions(self.get_inorder_traversal(root1), self.get_inorder_traversal(root2))
