# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/

from typing import List


class Solution:

    def get_freq_str(self, string):
        """
        Get char frequence for string
        """
        freq_str = [0] * 26
        for char in string:
            freq_str[ord(char) - ord('a')] += 1
        return freq_str

    def get_hash(self, string):
        """
        Returns anagrams hash
        """
        freq_str = self.get_freq_str(string)

        return "".join([chr(i + ord('a')) + str(freq_str[i]) for i in range(26)])

    def check_if_anagrams(self, str1, str2):
        """
        Function which checks if str1 and str2 are anagrams
        """
        return self.get_freq_str(str1) == self.get_freq_str(str2)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        anagram_dict = {}

        for string in strs:
            string_hash = self.get_hash(string)
            if string_hash not in anagram_dict:
                anagram_dict[string_hash] = [string]
            else:
                trial_string = anagram_dict[string_hash][-1]
                if self.check_if_anagrams(string, trial_string):
                    anagram_dict[string_hash].append(string)

        return anagram_dict.values()
