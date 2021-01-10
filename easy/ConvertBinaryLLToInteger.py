# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        num = 0
        for i in range(len(lst)):
            num = lst[i]*2**(len(lst) - i - 1)
        return num
