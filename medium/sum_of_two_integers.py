"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   10.04.2020 22:19
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a & mask if b > mask else a


for i in range(-100, 100):
    for j in range(-100, 100):
        if i + j != Solution().getSum(i, j):
            print(i, j, Solution().getSum(i, j))

print(Solution().getSum(10, -9))
