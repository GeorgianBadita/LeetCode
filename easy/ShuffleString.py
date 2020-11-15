# https://leetcode.com/problems/shuffle-string/submissions/

from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join([s[indices.index(i)] for i in range(len(s))])
