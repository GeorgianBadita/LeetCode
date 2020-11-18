# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

from typing import List


class Solution:

    def merge(self, lst, left, mid, right):
        cpy_first_half = []
        for i in range(left, mid + 1):
            cpy_first_half.append(lst[i])

        cpy_second_half = []
        for i in range(mid + 1, right + 1):
            cpy_second_half.append(lst[i])

        i = 0
        j = 0
        curr = left
        while i < len(cpy_first_half) and j < len(cpy_second_half):
            if cpy_first_half[i] > cpy_second_half[j]:
                lst[curr] = cpy_first_half[i]
                i += 1
            else:
                lst[curr] = cpy_second_half[j]
                j += 1
            curr += 1

        while i < len(cpy_first_half):
            lst[curr] = cpy_first_half[i]
            i += 1
            curr += 1

        while j < len(cpy_second_half):
            lst[curr] = cpy_second_half[j]
            j += 1
            curr += 1

    def merge_sort(self, lst, left, right):
        if left >= right:
            return
        else:
            mid = left + (right - left) // 2
            self.merge_sort(lst, left, mid)
            self.merge_sort(lst, mid + 1, right)
            self.merge(lst, left, mid, right)

    def maxCoins(self, piles: List[int]) -> int:
        self.merge_sort(piles, 0, len(piles) - 1)
        if len(piles) == 3:
            return piles[1]

        result = 0
        current_start = 0
        current_end = len(piles) - 1
        while current_start < current_end:
            result += piles[current_start + 1]
            current_end -= 1
            current_start += 2
        return result


Solution().maxCoins([2, 4, 1, 2, 7, 8])
