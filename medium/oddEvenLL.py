"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   01.04.2020 22:28
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        first_even = head
        first_odd = head.next
        first_odd_head = first_odd
        while first_even and first_odd:
            if not first_odd.next and length % 2 == 0:
                break
            if not first_even.next and length % 2 == 1:
                break
            next_even = first_even.next.next
            next_odd = first_odd.next.next
            first_even.next = next_even
            first_odd.next = next_odd
            first_even = first_even.next
            first_odd = first_odd.next

        first_even.next = first_odd_head
        return head


# (1->2->3->4->5)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)

new_head = Solution().oddEvenList(head)

while new_head:
    print(new_head.val)
    new_head = new_head.next
