# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/789/


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        root.next = None
        if not root.left and not root.right:
            return root

        queue = [(root, None)]

        while queue:
            curr_node, parent = queue.pop(0)
            if curr_node.left:
                queue.append((curr_node.left, curr_node))
            if curr_node.right:
                queue.append((curr_node.right, curr_node))
            if not parent:
                continue
            if parent.right:
                curr_node.next = parent.right
            elif parent.next:
                curr_node.next = parent.next.left
            else:
                parent.next = None

        return root

