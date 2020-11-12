# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # index for current element
        curr_index = 0

        for i in range(1, len(nums)):
            if nums[curr_index] != nums[i]:
                nums[curr_index + 1] = nums[i]
                curr_index += 1
        print(nums)
        return curr_index + 1

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

#[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#