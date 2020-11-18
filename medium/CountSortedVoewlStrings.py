# https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution:

    def __init__(self):
        self.__memo = {}

    def cnt(self, n, vowels):
        if n == 1:
            return vowels
        if vowels == 1:
            return 1

        if (n, vowels) in self.__memo:
            return self.__memo[(n, vowels)]

        return self.cnt(n - 1, vowels) + self.cnt(n, vowels - 1)

    def countVowelStrings(self, n: int) -> int:
        return self.cnt(n, 5)


print(Solution().countVowelStrings(50))
