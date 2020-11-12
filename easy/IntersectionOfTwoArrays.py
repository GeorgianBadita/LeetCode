# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/

from typing import List


class Solution:

    def find_sorted_intersection(self, list1, list2):
        if not list1 or not list2:
            return []

        if list1[0] == list2[0]:
            return [list1[0]] + self.find_sorted_intersection(list1[1:], list2[1:])
        else:
            if list1[0] < list2[0]:
                return self.find_sorted_intersection(list1[1:], list2)
            else:
                return self.find_sorted_intersection(list1, list2[1:])

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted_1 = sorted(nums1)
        sorted_2 = sorted(nums2)
        return self.find_sorted_intersection(sorted_1, sorted_2)


print(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]))
