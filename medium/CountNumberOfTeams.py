# https://leetcode.com/problems/count-number-of-teams/

from typing import List


class Solution:

    def get_comp_lists(self, rating):
        larger = [0]*len(rating)
        smaller = [0]*len(rating)

        for i in range(len(rating) - 1):
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    larger[i] += 1
                if rating[j] < rating[i]:
                    smaller[i] += 1
        return larger, smaller

    def get_teams(self, rating, comp_list, comp_type):

        num_teams = 0
        for i in range(len(rating) - 1):
            for j in range(i + 1, len(rating)):
                if comp_type == 'G':
                    if rating[j] > rating[i]:
                        num_teams += comp_list[j]
                elif comp_type == 'S':
                    if rating[j] < rating[i]:
                        num_teams += comp_list[j]
        return num_teams

    def numTeams(self, rating: List[int]) -> int:

        larger, smaller = self.get_comp_lists(rating)

        return self.get_teams(rating, larger, 'G') + self.get_teams(rating, smaller, 'S')
