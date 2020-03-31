"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 00:21
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for i in range(32):
            if n & 2 ** i:
                cnt += 1
        return cnt


print(Solution().hammingWeight(0))
