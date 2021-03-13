# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        if not boxes:
            return boxes

        if len(boxes) == 1:
            return [0]

        left = [0]
        cnt = 0 if boxes[0] == '0' else 1
        for i in range(1, len(boxes)):
            left.append(left[-1] + cnt)
            cnt += 1 if boxes[i] == '1' else 0

        right = [0] * len(boxes)
        cnt = 0 if boxes[-1] == '0' else 1

        for i in range(len(boxes) - 2, -1, -1):
            right[i] = right[i + 1] + cnt
            cnt += 1 if boxes[i] == '1' else 0
        return [left[i] + right[i] for i in range(len(boxes))]
