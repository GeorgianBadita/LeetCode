"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   19.04.2020 22:57
"""
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        next = [float('inf')] * 102
        res = [0] * len(T)
        for i in range(len(T) - 1, -1, -1):

            warm_index = min(next[t] for t in range(T[i] + 1, 102))

            if warm_index < float('inf'):
                res[i] = warm_index - i
            next[T[i]] = i

        return res


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
