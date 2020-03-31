"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 00:17
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return True if n > 0 and 1162261467 % n == 0 else False


print(3**19)
print(Solution().isPowerOfThree(3**19))