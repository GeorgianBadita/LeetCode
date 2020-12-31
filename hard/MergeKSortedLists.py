# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        resultList = None
        resListHead = None
        while len(heap) != 0:
            best, index = heapq.heappop(heap)
            if not resultList:
                resultList = ListNode(best)
                resListHead = resultList
            else:
                resultList.next = ListNode(best)
                resultList = resultList.next

            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))
                lists[index] = lists[index].next

        return resListHead


print(Solution().mergeKLists([]))
