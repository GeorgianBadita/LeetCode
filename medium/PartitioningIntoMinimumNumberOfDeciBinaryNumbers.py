class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(ord(x) - ord('0')) for x in n])
