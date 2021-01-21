# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return '$'

        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def construct(pos=0):
            if nodes[pos] == '$':
                return None, pos + 1

            node = TreeNode(nodes[pos])
            node.left, pos = construct(pos + 1)
            node.right, pos = construct(pos)

            return node, pos

        nodes = data.split(',')
        root, _ = construct()
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
