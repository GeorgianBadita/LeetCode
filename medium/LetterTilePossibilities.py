# https://leetcode.com/problems/letter-tile-possibilities/

class Solution:
    def __init__(self) -> None:
        self.__solution = set()
        self.__is_letter_usable = {}

    def generate(self, sol, candidates):
        for tile in candidates:
            if len(sol) + 1 <= len(candidates) and self.__is_letter_usable[tile] > 0:
                sol.append(tile)
                self.__is_letter_usable[tile] -= 1
                string_sol = ''.join(sol)
                if string_sol not in self.__solution:
                    self.__solution.add(string_sol)
                self.generate(sol, candidates)
                self.__is_letter_usable[tile] += 1
                sol.pop()

    def numTilePossibilities(self, tiles: str) -> int:
        for char in tiles:
            if char in self.__is_letter_usable:
                self.__is_letter_usable[char] += 1
            else:
                self.__is_letter_usable[char] = 1

        self.generate([], tiles)
        return len(self.__solution)


print(Solution().numTilePossibilities("ABCDEFG"))
