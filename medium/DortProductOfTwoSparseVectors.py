# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = [(i, nums[i]) for i in range(len(nums))]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0
        first_vec = self.vector
        second_vec = vec.vector

        p1 = 0
        p2 = 0
        while p1 < len(first_vec) and p2 < len(second_vec):
            if first_vec[p1][0] == second_vec[p2][0]:
                dot_product += first_vec[p1][1] * second_vec[p2][1]
                p1 += 1
                p2 += 1
            elif first_vec[p1][0] < second_vec[p2][0]:
                p1 += 1
            else:
                p2 += 1
        return dot_product

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)