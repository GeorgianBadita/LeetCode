# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        current_window = {s[0]: 0}
        current = 1
        best_length = current
        i = 1
        while i < len(s):
            if s[i] not in current_window:
                current_window[s[i]] = i
                current += 1
            else:
                i = current_window[s[i]] + 1
                if i < len(s):
                    current_window = {s[i]: i}
                if current > best_length:
                    best_length = current
                current = 1
            i += 1

        return best_length if best_length > current else current


print(Solution().lengthOfLongestSubstring("aaaaabasdr"))
