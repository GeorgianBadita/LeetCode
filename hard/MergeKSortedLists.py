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
        finished = [False if head is not None else True for head in lists]

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
                if not lists[i]:
                    finished[i] = True

        if False not in finished and len(heap) == 0:
            return None

        resultList = None
        resListHead = None
        while True:
            best, index = heapq.heappop(heap)
            if not resultList:
                resultList = ListNode(best)
                resListHead = resultList
            else:
                resultList.next = ListNode(best)
                resultList = resultList.next

            if not lists[index]:
                finished[index] = True
            else:
                heapq.heappush(heap, (lists[index].val, index))
                lists[index] = lists[index].next

            if False not in finished and len(heap) == 0:
                break

        return resListHead


print(Solution().mergeKLists([]))
