"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   01.04.2020 22:18
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val + l2.val > 9:
            carry = 1
            result = ListNode((l1.val + l2.val) % 10)
        else:
            carry = 0
            result = ListNode(l1.val + l2.val)
        init_head = result
        head1 = l1.next
        head2 = l2.next
        while head1 or head2:
            next_node = ListNode(None)
            if head1 and head2:
                val = head1.val + head2.val + carry
                carry = val // 10
                val %= 10
                next_node.val = val
                head1 = head1.next
                head2 = head2.next
            elif not head1:
                val = head2.val + carry
                carry = val // 10
                val %= 10
                next_node.val = val
                head2 = head2.next
            elif not head2:
                val = head1.val + carry
                carry = val // 10
                val %= 10
                next_node.val = val
                head1 = head1.next
            result.next = next_node
            result = next_node
        if carry:
            result.next = ListNode(1)
        return init_head


# (2 -> 4 -> 3) + (5 -> 6 -> 4)
head1 = ListNode(2)
head1.next = ListNode(4)
head1.next.next = ListNode(3)

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(4)

sum_head = Solution().addTwoNumbers(head1, head2)

while sum_head:
    print(sum_head.val)
    sum_head = sum_head.next
