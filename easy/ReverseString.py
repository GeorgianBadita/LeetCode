# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/

from typing import List


class Solution:

    def helper(self, lst, left, right):
        if left >= right:
            return
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
        self.helper(lst, left, right)

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.helper(s, 0, len(s) - 1)
        return s

print(Solution().reverseString(['a', 'b', 'c']))