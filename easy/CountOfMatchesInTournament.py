# https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution:
    def numberOfMatches(self, n: int) -> int:
        sum_ = 0

        while n != 1:
            sum_ += int(n / 2)
            n = int(n / 2) + 1 if n % 2 == 1 else int(n / 2)
        return sum_


print(Solution().numberOfMatches(14))
