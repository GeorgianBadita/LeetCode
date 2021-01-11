# https://leetcode.com/problems/to-lower-case/

class Solution:
    def toLowerCase(self, str: str) -> str:
        A = ord('A')
        Z = ord('Z')
        a = ord('a')
        return ''.join([chr(ord(x) + (a - A)) if A <= ord(x) <= Z else x for x in str])
