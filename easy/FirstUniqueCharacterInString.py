# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        if len(s) == 1:
            return 0

        freq_dict = {}

        for index in range(len(s)):
            if s[index] in freq_dict:
                freq_dict[s[index]] = -1
            else:
                freq_dict[s[index]] = index
        lowest_index = len(s)
        for key, value in freq_dict.items():
            if value < lowest_index and value != -1:
                lowest_index = value

        return lowest_index if lowest_index != len(s) else -1


print(Solution().firstUniqChar("aadadaad"))
