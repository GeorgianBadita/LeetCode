# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/815/

class Solution:

    def compute_squared_sum(self, n):
        sq_sum = 0
        while n > 0:
            sq_sum += (n % 10)**2
            n //= 10

        return sq_sum

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        tortoise = self.compute_squared_sum(n)
        hare = self.compute_squared_sum(tortoise)

        while True:
            if hare == 1 or tortoise == 1:
                return True
            if hare == tortoise:
                return False

            tortoise = self.compute_squared_sum(tortoise)
            hare = self.compute_squared_sum(self.compute_squared_sum(hare))
