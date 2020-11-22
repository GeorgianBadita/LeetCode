# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/submissions/

class Solution:

    def get_freq(self, s):
        freq = [0]*26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        return freq

    def minSteps(self, s: str, t: str) -> int:
        freq_s = self.get_freq(s)
        freq_t = self.get_freq(t)

        diff = 0
        for i in range(26):
            if freq_s[i] > freq_t[i]:
                diff += freq_s[i] - freq_t[i]
        return diff
