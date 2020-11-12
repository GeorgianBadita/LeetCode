# https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/744/


class Solution:

    def sieve(self, n):
        # there are no primes < 2
        if n <= 2:
            return 0
        # if n is 3 there is only one prime number - 2
        if n == 3:
            return 1

        is_prime = [True if num % 2 == 1 and num > 1 else False for num in range(n)]
        is_prime[2] = True

        for i in range(3, n, 2):
            if is_prime[i]:
                for j in range(2 * i, n, i):
                    is_prime[j] = False

        i = 0
        for prime in is_prime:
            if prime:
                print(i)
            i += 1
        return sum(is_prime)

    def countPrimes(self, n: int) -> int:
        return self.sieve(n)

Solution().sieve(10)