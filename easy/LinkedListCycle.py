# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # if the list has 0 or 1 nodes it cannot have a cycle
        if not head or not head.next:
            return False

        # use hare and tortoise algorithm
        tortoise = head
        hare = head.next

        while hare is not None and tortoise is not None:
            if hare.val == tortoise.val:
                return True

            if not tortoise.next:
                return False
            else:
                tortoise = tortoise.next

            if not hare.next or not hare.next.next:
                return False
            else:
                hare = hare.next.next

        return False
