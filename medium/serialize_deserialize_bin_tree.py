"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   10.04.2020 20:41
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        serializ = ''
        queue = [root]

        while len(queue) > 0:
            node = queue[0]
            queue.pop(0)
            if not node:
                serializ += 'None,'
            else:
                serializ += str(node.val) + ','
                queue.append(node.left)
                queue.append(node.right)

        return serializ[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        tree_lst = data.split(',')
        root = TreeNode(int(tree_lst[0]))
        index = 1
        queue = [root]
        while len(queue) > 0:
            node = queue[0]
            queue.pop(0)
            left = tree_lst[index]
            right = tree_lst[index + 1]
            if left != 'None':
                node.left = TreeNode(int(left))
                queue.append(node.left)
            if right != 'None':
                node.right = TreeNode(int(right))
                queue.append(node.right)

            index += 2
            if index > len(tree_lst):
                break

        return root


# [5,2,3,null,null,2,4,3,1]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)


# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.serialize(root))
root = codec.deserialize(codec.serialize(root))

print()
