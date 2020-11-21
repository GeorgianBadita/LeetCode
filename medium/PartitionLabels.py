# https://leetcode.com/problems/partition-labels/

from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_for_letter = {s: None for s in set(S)}
        for i in range(len(S)):
            last_for_letter[S[i]] = i

        i = 0
        result = []
        while i < len(S):
            start = i
            end = last_for_letter[S[start]]
            j = start
            while j < end:
                end = max(end, last_for_letter[S[j]])
                j += 1
            i = end + 1
            result.append(end - start + 1)
        return result


Solution().partitionLabels("ababcbacadefegdehijhklij")
