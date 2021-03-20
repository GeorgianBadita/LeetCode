# https://leetcode.com/problems/nested-list-weight-sum/

from typing import List

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution:

    def depth_sum_aux(self, nested_list, depth):
        if not nested_list:
            return 0

        head, tail = nested_list[0], nested_list[1:]
        if head.isInteger():
            return depth*head.getInteger() + self.depth_sum_aux(tail, depth)

        return self.depth_sum_aux(head.getList(), depth + 1) + self.depth_sum_aux(tail, depth)

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        print(nestedList)
        return self.depth_sum_aux(nestedList, 1)
