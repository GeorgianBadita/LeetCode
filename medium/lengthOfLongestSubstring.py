"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   28.03.2020 22:14
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        if len(s) == 2:
            if s[0] != s[1]:
                return 2
            return 1

        longest = 0
        max_longest = 0
        freq = {}
        i = 0
        while i < len(s):
            if s[i] not in freq:
                longest += 1
                freq[s[i]] = i
            else:
                if longest > max_longest:
                    max_longest = longest
                if freq[s[i]] + 1 < len(s):
                    i = freq[s[i]] + 1
                freq = {s[i]: i}
                longest = 1
            i += 1

        if longest > max_longest:
            max_longest = longest
        return max_longest


print(Solution().lengthOfLongestSubstring("aaaaaaaaa"))
