# https://leetcode.com/submissions/detail/427458109/


class Solution:
    def construct_contest_matches(self, n, pow2):
        if pow2 == 2:
            return [f"({i},{n - i + 1})" for i in range(1, n // 2 + 1)]

        last_level = self.construct_contest_matches(n, pow2 // 2)
        return [
            f"({last_level[i]},{last_level[len(last_level) - i - 1]})"
            for i in range(len(last_level) // 2)
        ]

    def findContestMatch(self, n: int) -> str:
        return self.construct_contest_matches(n, n)