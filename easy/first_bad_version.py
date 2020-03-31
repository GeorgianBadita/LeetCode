"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 22:25
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version >= 3:
        return True
    return False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            is_mid_bad = isBadVersion(mid)
            if is_mid_bad:
                right = mid
            else:
                left = mid + 1
        return left

print(Solution().firstBadVersion(6))
