# https://leetcode.com/problems/find-and-replace-pattern/

from typing import List


class Solution:
    def can_find_mapping(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping = {}
        for i in range(len(s)):
            if t[i] in mapping and mapping[t[i]] != s[i]:
                return False
            for key, value in mapping.items():
                if value == s[i] and key != t[i]:
                    return False
            mapping[t[i]] = s[i]
        return True

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return [x for x in words if self.can_find_mapping(x, pattern)]