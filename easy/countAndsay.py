"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   29.03.2020 23:35
"""

def get_next(curr_elem):
    i = 0
    new_elem = ""
    while i < len(curr_elem):
        cnt = 0
        while i + 1 < len(curr_elem) and curr_elem[i] == curr_elem[i + 1]:
            cnt += 1
            i += 1
        new_elem += str(cnt + 1) + curr_elem[i]
        i += 1
    return new_elem

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        elem = '11'
        for i in range(3, n + 1):
            elem = get_next(elem)
        return elem

print(Solution().countAndSay(5))