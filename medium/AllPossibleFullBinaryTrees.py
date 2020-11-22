# https://leetcode.com/problems/all-possible-full-binary-trees/

from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.__sols = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N in self.__sols:
            return self.__sols[N]

        ans = []
        for x in range(N):
            y = N - x - 1
            for left in self.allPossibleFBT(x):
                for right in self.allPossibleFBT(y):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ans.append(root)
        self.__sols[N] = ans
        return self.__sols[N]

Solution().allPossibleFBT(5)