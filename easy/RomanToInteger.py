# https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/878/


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        num = 0
        start = 0
        while start < len(s):
            if start + 1 < len(s) and roman_to_int[s[start]] < roman_to_int[s[start + 1]]:
                to_diff = 0
                cnt = 1
                while start + 1 < len(s) and roman_to_int[s[start]] < roman_to_int[s[start + 1]] and cnt < 4:
                    to_diff += roman_to_int[s[start]]
                    start += 1
                    cnt += 1
                if start < len(s):
                    num += roman_to_int[s[start]] - to_diff
                    start += 1
            else:
                num += roman_to_int[s[start]]
                start += 1
        return num


print(Solution().romanToInt("MCMXCIV"))
