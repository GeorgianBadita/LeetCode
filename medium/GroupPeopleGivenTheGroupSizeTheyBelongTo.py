# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

from typing import List, get_args


class Solution:

    def create_by_group_size(self, gr_list):
        freq_dict = {}
        for i in range(len(gr_list)):
            if gr_list[i] not in freq_dict:
                freq_dict[gr_list[i]] = [i]
            else:
                freq_dict[gr_list[i]].append(i)
        return freq_dict

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        grpup_by_size = self.create_by_group_size(groupSizes)
        result = []

        for group_size, preference in grpup_by_size.items():
            for i in range(0, len(preference), group_size):
                current_group = []
                for j in range(i, i + group_size):
                    current_group.append(preference[j])
                result.append(current_group)

        return result
