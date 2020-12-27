# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num_stirngs = 0
        balanced = 1 if s[0] == 'L' else -1
        i = 1
        while i < len(s):
            balanced += 1 if s[i] == 'L' else -1

            if balanced == 0:
                num_stirngs += 1
                if i + 1 < len(s):
                    balanced = 1 if s[i + 1] == 'L' else -1
                i += 1

            i += 1

        return num_stirngs
