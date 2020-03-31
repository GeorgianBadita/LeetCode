"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 00:09
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        rez = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                rez.append("FizzBuzz")
            elif i % 3 == 0:
                rez.append("Fizz")
            elif i % 5 == 0:
                rez.append("Buzz")
            else:
                rez.append(str(i))
        return rez


print(Solution().fizzBuzz(15))
