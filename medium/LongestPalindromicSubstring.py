# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or not s:
            return s
        if len(s) == 2:
            if s[0] == s[-1]:
                return s
            else:
                return s[0]

        i = 0
        start = -1
        max_length = -1
        while i < len(s):
            # check for even length palindrome
            if i + 1 < len(s) and s[i] == s[i + 1]:
                length = 1
                while i + length < len(s) and i - length + 1 >= 0 and s[i - length + 1] == s[i + length]:
                    length += 1
                # real length of palindrome
                if (length - 1) * 2 > max_length:
                    max_length = (length - 1) * 2
                    start = i - length + 2

            # check for odd length palindrome
            if i + 1 < len(s) and i - 1 >= 0 and s[i + 1] == s[i - 1]:
                length = 1
                while i + length < len(s) and i - length >= 0 and s[i - length] == s[i + length]:
                    length += 1

                # real length of palindrome
                if 2 * length - 1 > max_length:
                    max_length = 2 * length - 1
                    start = i - length + 1

            i += 1

        return s[start:start + max_length] if start >= 0 else s[-1]


print(Solution().longestPalindrome("bab"))
