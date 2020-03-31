"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   29.03.2020 02:15
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        if len(s) == 1:
            return 0

        char_freq = [0] * 26
        for char in s:
            char_freq[ord(char) - ord('a')] += 1

        for i in range(len(s)):
            if char_freq[ord(s[i]) - ord('a')] == 1:
                return i
        return -1


print(Solution().firstUniqChar("leetcode"))
