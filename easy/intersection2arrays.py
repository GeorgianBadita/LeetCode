"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   29.03.2020 00:00
"""
from typing import List


def bsrch_first(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return True
        if arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1

    return False


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        intersection = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return intersection


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(Solution().intersect(nums1, nums2))
