"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   12.04.2020 00:39
"""
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor_table = [arr[0]]
        for i in range(1, len(arr)):
            xor_table.append(xor_table[-1] ^ arr[i])

        def query(a, b):
            if a == 0:
                return xor_table[b]
            return xor_table[b] ^ xor_table[a - 1]

        return [query(a, b) for a, b in queries]


print(Solution().xorQueries([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]]))
