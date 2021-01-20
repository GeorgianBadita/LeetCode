# https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number(self, num: int) -> int:
        num_cpy = num
        last_6 = None

        poz = 0
        while num_cpy > 0:
            if num_cpy % 10 == 6:
                last_6 = poz
            poz += 1
            num_cpy = int(num_cpy / 10)

        if last_6 is None:
            return num
        result = 0
        pow_10 = 1
        poz = last_6
        while num != 0:
            if poz == 0:
                result = 9 * pow_10 + result
            else:
                result = (num % 10) * pow_10 + result
            num = int(num / 10)
            pow_10 *= 10
            poz -= 1
        return result
