# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/819/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x

        start = 0
        end = x // 2 + 1

        while start < end:

            mid = (end + start + 1) // 2
            if (mid + 1) ** 2 > x and mid**2 <= x:
                return mid
            if mid ** 2 > x:
                end = mid - 1
            else:
                start = mid


print(Solution().mySqrt(16))
