"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   11.04.2020 18:44
"""
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        freq = sorted(freq)
        time = 0
        while freq[25] > 0:
            i = 0
            while i <= n:
                if freq[25] == 0:
                    break
                if i < 26 and freq[25 - i] > 0:
                    freq[25 - i] -= 1
                time += 1
                i += 1

            freq = sorted(freq)
        return time


print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))
