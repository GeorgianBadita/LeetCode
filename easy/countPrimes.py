"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 00:11
"""


def sieve(n):
    primes = [1 if x % 2 == 1 and x > 2 else 0 for x in range(n)]
    primes[2] = 1

    for i in range(3, n, 2):
        if primes[i] is 1:
            for j in range(i + i, n, i):
                primes[j] = 0

    return sum(primes)


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        return sieve(n)

