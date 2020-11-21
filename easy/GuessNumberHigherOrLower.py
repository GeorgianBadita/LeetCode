# https://leetcode.com/explore/learn/card/binary-search/125/template-i/951/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

pick = 6


def guess(num):
    if pick == num:
        return 0
    if pick < num:
        return -1
    return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            guess_response = guess(mid)
            if guess_response == 1:
                left = mid + 1
            elif guess_response == -1:
                right = mid - 1
            else:
                return mid

print(Solution().guessNumber(10))
