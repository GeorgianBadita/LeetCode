# https://leetcode.com/problems/count-the-number-of-consistent-strings/

from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        num_consistent = 0
        for word in words:
            consistent = True
            for char in word:
                if char not in allowed:
                    consistent = False
                    break
            if consistent:
                num_consistent += 1
        return num_consistent
