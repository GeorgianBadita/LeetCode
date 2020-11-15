# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps (self, num: int) -> int:
        num_steps = 0
        while num:
            num_steps += 1
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
        return num_steps