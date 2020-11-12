# https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/825/

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

def knows(a, b):
    mat = [[1, 0, 1], [1, 1, 1], [0, 0, 1]]
    return mat[a][b]


class Solution:

    def find_celeb_dfs(self, n):
        candidates = [0]
        impossible_candidates = set()
        cache = [[None for __ in range(n)] for _ in range(n)]
        vis = [False]*n

        while candidates:
            current_candidate = candidates.pop()
            vis[current_candidate] = True
            is_celeb = True
            for adj in range(n):
                if current_candidate == adj:
                    continue

                current_candidate_knows_adj = cache[current_candidate][adj]
                if current_candidate_knows_adj is None:
                    current_candidate_knows_adj = knows(current_candidate, adj)
                    cache[current_candidate][adj] = current_candidate_knows_adj

                adj_knows_current_candidate = cache[adj][current_candidate]
                if adj_knows_current_candidate is None:
                    adj_knows_current_candidate = knows(adj, current_candidate)
                    cache[adj][current_candidate] = adj_knows_current_candidate

                if not current_candidate_knows_adj and adj_knows_current_candidate:
                    impossible_candidates.add(adj)
                else:
                    impossible_candidates.add(current_candidate)
                    if not vis[adj]:
                        candidates.append(adj)
                    is_celeb = False

            if is_celeb:
                return current_candidate
        return -1

    def findCelebrity(self, n: int) -> int:
        return self.find_celeb_dfs(n)


print(Solution().findCelebrity(3))
