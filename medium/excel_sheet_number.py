"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   06.04.2020 23:19
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        # TODO (WRONG)
        if len(s) == 1:
            return ord(s[0]) - ord('A') + 1
        cell = 0
        for i in range(len(s) - 1):
            cell += 26 * (ord(s[i]) - ord('A') + 1)
        return cell + ord(s[-1]) - ord('A') + 1


print(Solution().titleToNumber("ZYY"))
