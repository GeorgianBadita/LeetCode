"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   04.04.2020 23:31
"""
from typing import List


def is_consistent(par, n, o, c):
    num_open = o
    num_closed = c

    if par == ')':
        if num_closed + 1 > n // 2 or num_closed + 1 > num_open:
            return False
    if par == '(':
        if num_open + 1 > n // 2:
            return False
    if num_open > n // 2 or num_closed > n // 2:
        return False

    return True


def is_sol(sol, n):
    return len(sol) == n


def gen_par(sol, n, sols, o, c):
    for par in '()':
        if is_consistent(par, n, o, c):
            sol += par
            if par == '(':
                o += 1
            else:
                c += 1
            if is_sol(sol, n):
                sols.append(sol)
            gen_par(sol,  n, sols, o, c)
            if sol[-1] == ')':
                c -= 1
            else:
                o -= 1
            sol = sol[:-1]


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sols = []
        gen_par("" , 2 * n, sols, 0, 0)
        return sols


print(Solution().generateParenthesis(3))
