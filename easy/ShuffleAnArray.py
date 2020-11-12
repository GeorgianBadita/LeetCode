# https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/

from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.__org_nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.__org_nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        indexes = [i for i in range(len(self.__org_nums))]
        shuffle_array = []
        for _ in range(len(self.__org_nums)):
            rand_ind = random.choice(indexes)
            indexes.remove(rand_ind)
            shuffle_array.append(self.__org_nums[rand_ind])
        return shuffle_array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
