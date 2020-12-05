# https://leetcode.com/submissions/detail/427452757/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def parent_dict(self, root):
        parent = {root: None}
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
        return parent

    def lca(self, x, y, parent_dict):
        x_set = {x}
        while x:
            x_set.add(parent_dict[x])
            x = parent_dict[x]

        while y:
            if y in x_set:
                return y
            y = parent_dict[y]

    def compute_list_lca(self, nodes_list, parent_dict):
        return (
            nodes_list[0]
            if len(nodes_list) == 1
            else self.lca(
                nodes_list[0],
                self.compute_list_lca(nodes_list[1:], parent_dict),
                parent_dict,
            )
        )

    def lowestCommonAncestor(
        self, root: "TreeNode", nodes: "List[TreeNode]"
    ) -> "TreeNode":
        parent_dict = self.parent_dict(root)
        return self.compute_list_lca(nodes, parent_dict)
