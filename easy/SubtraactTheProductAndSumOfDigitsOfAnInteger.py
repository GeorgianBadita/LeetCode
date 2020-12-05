# https://leetcode.com/submissions/detail/427466037/


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_d = 0
        prod_d = 1
        while n > 0:
            sum_d += n % 10
            prod_d *= n % 10
            n = int(n / 10)

        return prod_d - sum_d