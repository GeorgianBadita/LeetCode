"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   06.04.2020 22:20
"""


class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0 or x == 1:
            return x

        low = 0
        high = x // 2
        while low <= high:
            mid = low + (high - low) // 2

            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1

        return low - 1


print(Solution().mySqrt(121))
