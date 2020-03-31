"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   28.03.2020 21:47
"""
from typing import List


def hash_word(word: str):
    freq = [0] * 26
    for char in word:
        freq[ord(char) - ord('a')] += 1

    hash = 0
    pow = 0
    for i in range(25, -1, -1):
        hash += freq[i] * (26 ** pow)
        pow += 1

    return hash


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol_map = {}
        for word in strs:
            word_hash = hash_word(word)
            if word_hash in sol_map:
                sol_map[word_hash].append(word)
            else:
                sol_map[word_hash] = [word]

        return list(sol_map.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
