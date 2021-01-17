# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        current_index_s = 0

        for char in t:
            if current_index_s < len(s) and char == s[current_index_s]:
                current_index_s += 1
        return current_index_s == len(s)
