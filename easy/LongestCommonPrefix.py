# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        longest_prefix = strs[0]
        for i in range(1, len(strs)):
            curr_str = strs[i]
            ind_curr_longest = 0
            ind_curr_str = 0
            while ind_curr_longest < len(longest_prefix) and ind_curr_str < len(curr_str) and longest_prefix[ind_curr_longest] == curr_str[ind_curr_str]:
                ind_curr_longest += 1
                ind_curr_str += 1

            longest_prefix = longest_prefix[:ind_curr_str]

        return longest_prefix
