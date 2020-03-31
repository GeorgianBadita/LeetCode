"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   01.04.2020 00:00
"""
from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.__original = nums
        self.__array = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.__array = list(self.__original)
        return self.__original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """

        for i in range(len(self.__original)):
            id_to_remove = random.randrange(i, len(self.__array))
            self.__array[i], self.__array[id_to_remove] = self.__array[id_to_remove], self.__array[i]

        return self.__array


sol = Solution([1, 2, 3])

sol.reset()

print(sol.shuffle())
