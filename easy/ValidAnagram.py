# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = [0]*26
        freq_t = [0]*26

        for char in s:
            freq_s[ord(char) - ord('a')] += 1

        for char in t:
            freq_t[ord(char) - ord('a')] += 1

        for i in range(26):
            if freq_t[i] != freq_s[i]:
                return False
        return True
