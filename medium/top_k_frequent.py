"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   05.04.2020 22:04
"""
import collections
import heapq
from collections import namedtuple
from typing import List

Element = namedtuple('Element', ['value', 'priority'])


class Heap:
    def __init__(self):
        self.__heap = []

    def get_heap(self):
        return self.__heap

    def add(self, elem: Element) -> None:
        self.__heap.append(elem)
        self.__heapify_up(len(self.__heap) - 1)

    def __heapify_up(self, index):
        while True:
            parent = self.__get_parent(index)
            if parent is None:
                break
            if self.__heap[parent].priority > self.__heap[index].priority:
                self.__heap[parent], self.__heap[index] = self.__heap[index], self.__heap[parent]
                index = parent
            else:
                break

    def extract_min(self):
        if len(self.__heap) == 0:
            return None
        to_return = self.__heap[0]
        self.__heap[0] = self.__heap[-1]
        self.__heap.pop()
        self.__heapify_down(0)
        return to_return

    def __heapify_down(self, index):
        while True:
            if index == len(self.__heap) - 1:
                return
            left = self.__get_left_child(index)
            right = self.__get_right_child(index)
            if left >= len(self.__heap) and right >= len(self.__heap):
                break
            to_chose = None
            if right >= self.size > left:
                to_chose = left
            if right >= len(self.__heap) > left:
                to_chose = left
            elif left and right:
                if self.__heap[left].priority < self.__heap[right].priority:
                    to_chose = left
                else:
                    to_chose = right
            if not to_chose:
                break
            if self.__heap[index].priority > self.__heap[to_chose].priority:
                self.__heap[index], self.__heap[to_chose] = self.__heap[to_chose], self.__heap[index]
                index = to_chose
            else:
                break

    def __get_parent(self, i):
        if i == 0:
            return None
        return (i - 1) // 2

    def __get_left_child(self, i):
        return 2 * i + 1

    def __get_right_child(self, i):
        return 2 * i + 2

    def get_top(self):
        if len(self.__heap) == 0:
            return None
        return self.__heap[0]

    @property
    def size(self):
        return len(self.__heap)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for elem in nums:
            freq[elem] = freq.get(elem, 0) + 1
        hp = Heap()
        for key in freq:
            hp.add(Element(value=key, priority=freq[key]))
            if hp.size > k:
                hp.extract_min()

        return list(reversed([hp.extract_min().value for _ in range(k)]))


class Solution2:
    def topKFrequent(self, nums, k):
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), count.get)


nums = [1, 122, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 3, 3, 3]
k = 3

print(Solution2().topKFrequent(nums, k))
