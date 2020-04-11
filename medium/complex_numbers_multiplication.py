"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   11.04.2020 23:26
"""


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        x, y = int(a.split('+')[0]), int(a.split('+')[1][:-1])
        c, d = int(b.split('+')[0]), int(b.split('+')[1][:-1])

        x_sum = x * c - y * d
        y_sum = y * c + d * x

        return f"{str(x_sum)}+{str(y_sum)}i"


print(Solution().complexNumberMultiply("1+-1i", "1+-1i"))
