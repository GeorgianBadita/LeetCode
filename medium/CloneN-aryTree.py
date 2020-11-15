# https://leetcode.com/problems/clone-n-ary-tree/


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        clone = Node(root.val)
        result_clone = clone
        queue = [root]
        clone_queue = [clone]

        while queue:
            curr_node = queue.pop(0)
            curr_node_clone = clone_queue.pop(0)
            for child in curr_node.children:
                new_child = Node(child.val)
                queue.append(child)
                curr_node_clone.children.append(new_child)
                clone_queue.append(new_child)

        return result_clone

tree = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
Solution().cloneTree(tree)