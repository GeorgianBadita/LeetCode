# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/


from typing import List


class MinHeap:

    def __init__(self, k):
        self.__heap = [None] * (k + 1)
        self.__current = 0

    def add_element(self, elem):
        self.__heap[self.__current] = elem
        self.__heapify_up()
        self.__current += 1

    def pop_min(self):
        if self.__current == 0:
            return None
        min_element = self.__heap[0]
        self.__heap[0] = self.__heap[self.__current - 1]
        self.__current -= 1
        self.__heapify_down()
        return min_element

    def get_heap_array(self):
        return self.__heap

    def get_heap_count(self):
        return self.__current

    def __heapify_down(self):
        current_index = 0
        satisfies_relation = False
        while not satisfies_relation and current_index < len(self.__heap):
            satisfies_relation = True
            left_child_index = self.__get_left_child(current_index)
            right_child_index = self.__get_right_child(current_index)

            to_go_index = None
            if left_child_index and right_child_index:
                if self.__heap[left_child_index][1] < self.__heap[right_child_index][1]:
                    to_go_index = left_child_index
                else:
                    to_go_index = right_child_index
            elif left_child_index:
                to_go_index = left_child_index
            elif right_child_index:
                to_go_index = right_child_index
            else:
                break

            if self.__heap[current_index][1] > self.__heap[to_go_index][1]:
                self.__heap[current_index], self.__heap[to_go_index] = self.__heap[to_go_index], self.__heap[current_index]
                current_index = to_go_index
                satisfies_relation = False
            else:
                satisfies_relation = True

    def __heapify_up(self):
        current_index = self.__current
        respects_relationship = False
        while not respects_relationship and current_index > 0:
            respects_relationship = True
            parent_index = self.__get_parent(current_index)
            if parent_index is None:
                break
            current_element = self.__heap[current_index][1]
            parent_element = self.__heap[parent_index][1]
            if current_element < parent_element:
                self.__heap[current_index], self.__heap[parent_index] = self.__heap[parent_index], self.__heap[current_index]
                current_index = parent_index
                respects_relationship = False

    def __get_parent(self, pos):
        if pos > self.__current or pos == 0:
            return None

        return pos // 2 - 1 if pos % 2 == 0 else pos // 2

    def __get_left_child(self, pos):
        return None if 2 * pos + 1 > self.__current else 2 * pos + 1

    def __get_right_child(self, pos):
        return None if 2 * pos + 2 > self.__current else 2 * pos + 2


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = MinHeap(k)

        freq_dict = {}
        for elem in nums:
            if elem not in freq_dict:
                freq_dict[elem] = 1
            else:
                freq_dict[elem] += 1

        for elem, freq in freq_dict.items():

            heap.add_element((elem, freq))
            if heap.get_heap_count() == k + 1:
                heap.pop_min()

        return [elem[0] for elem in heap.get_heap_array()[:k]]


print(Solution().topKFrequent([1], 1))
