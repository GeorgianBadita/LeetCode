# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if len(haystack) == len(needle):
            return 0 if haystack == needle else -1

        # was too late in the day to implement Rabin Karp or KMP
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                found = True
                for j in range(len(needle)):
                    if haystack[i + j] != needle[j]:
                        found = False
                        break
                if found:
                    return i
        return -1
