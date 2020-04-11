"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   11.04.2020 22:38
"""
from typing import List


class Solution:

    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xx = 1
        pows_x = [xx]
        while xx <= bound and xx * x > xx:
            xx *= x
            pows_x.append(xx)

        yy = 1
        pows_y = [yy]
        while yy <= bound and yy * y > yy:
            yy *= y
            pows_y.append(yy)

        pow_set = set()
        for xx in pows_x:
            for yy in pows_y:
                if xx + yy <= bound:
                    pow_set.add(xx + yy)

        return sorted(list(pow_set))


print(Solution().powerfulIntegers(2, 3, 10))
