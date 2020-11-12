# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/784/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head

        odd_head = head
        even_head = head.next
        copy_even = even_head

        while even_head:
            if odd_head and odd_head.next:
                odd_head.next = odd_head.next.next
            if even_head and even_head.next:
                even_head.next = even_head.next.next
            if odd_head.next:
                odd_head = odd_head.next
            even_head = even_head.next

        odd_head.next = copy_even
        return head
