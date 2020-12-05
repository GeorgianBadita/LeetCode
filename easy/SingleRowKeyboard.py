# https://leetcode.com/problems/single-row-keyboard/


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        current_pos = 0
        result = 0
        for char in word:
            current_char_index = keyboard.index(char)
            result += abs(current_char_index - current_pos)
            current_pos = current_char_index
        return result