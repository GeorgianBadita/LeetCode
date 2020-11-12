# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ahead_pointer = head
        for i in range(n):
            ahead_pointer = ahead_pointer.next

        if ahead_pointer is None:
            return head.next

        node_to_del = head
        while ahead_pointer.next is not None:
            ahead_pointer = ahead_pointer.next
            node_to_del = node_to_del.next

        node_to_del.next = node_to_del.next.next

        return head


ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
ll.next.next.next.next = ListNode(5)

Solution().removeNthFromEnd(ll, 5)
