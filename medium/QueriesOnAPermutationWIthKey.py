# https://leetcode.com/problems/queries-on-a-permutation-with-key/


from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:

        permutation = {i + 1: i for i in range(m)}

        result = []

        for query in queries:
            index = permutation[query]
            result.append(index)

            for key in permutation:
                if permutation[key] < index:
                    permutation[key] += 1
                elif permutation[key] == index:
                    permutation[key] = 0
        return result


print(Solution().processQueries([3, 1, 2, 1], 5))