# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/submissions/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: TreeNode):
        self.__tree_root = root
        self.__restore_tree()
        self.__cached_responses = set()
        self.__find_nodes(self.__tree_root)

    def __restore_tree(self):
        self.__tree_root.val = 0
        queue = [self.__tree_root]
        while queue:
            node = queue.pop(0)

            if node.left:
                node.left.val = 2 * node.val + 1
                queue.append(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                queue.append(node.right)

    def __find_nodes(self, root):
        if not root:
            return
        self.__cached_responses.add(root.val)
        self.__find_nodes(root.left)
        self.__find_nodes(root.right)

    def find(self, target: int) -> bool:
        return target in self.__cached_responses


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)