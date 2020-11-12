# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def add_beginning(self, node, llist):
        node.next = llist
        return node

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # if l1 is empty return l2
        if not l1:
            return l2

        # if l2 is empty return l1
        if not l2:
            return l1

        return self.add_beginning(ListNode(l1.val),
                                  self.mergeTwoLists(l1.next, l2)) if l1.val < l2.val else self.add_beginning(
            ListNode(l2.val), self.mergeTwoLists(l1, l2.next))
