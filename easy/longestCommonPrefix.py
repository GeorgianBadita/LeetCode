"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   29.03.2020 23:02
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        max_prefix = strs[0]
        i = 0
        for curr_letter in max_prefix:
            for string in strs:
                if i == len(string) or string[i] != curr_letter:
                    return max_prefix[0:i]
            i += 1
        return max_prefix


print(Solution().longestCommonPrefix(["aa", "a"]))
