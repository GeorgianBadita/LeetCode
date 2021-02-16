# https://leetcode.com/problems/intersection-of-three-sorted-arrays/submissions/

from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        intersection = []

        p1 = 0
        p2 = 0
        p3 = 0

        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            if arr1[p1] == arr2[p2] == arr3[p3]:
                intersection.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            elif min([arr1[p1], arr2[p2], arr3[p3]]) == arr1[p1]:
                p1 += 1
            elif min([arr1[p1], arr2[p2], arr3[p3]]) == arr2[p2]:
                p2 += 1
            elif min([arr1[p1], arr2[p2], arr3[p3]]) == arr3[p3]:
                p3 += 1

        return intersection
