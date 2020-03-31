"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   30.03.2020 23:43
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def revert_linked_list(head):
    if not head or not head.next:
        return head
    curr = head
    first = head
    next = head.next
    while next:
        curr1 = next
        next = next.next
        curr1.next = curr
        curr = curr1
    first.next = None
    return curr1


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        num_elements = 0
        tmp = head
        while tmp is not None:
            tmp = tmp.next
            num_elements += 1
        if num_elements == 2:
            if head.val != head.next.val:
                return False
            return True
        half = num_elements // 2

        tmp = head
        for _ in range(half):
            tmp = tmp.next
        if num_elements % 2 == 1:
            tmp = tmp.next
        half_rev = revert_linked_list(tmp)
        for _ in range(half):
            if half_rev.val != head.val:
                return False
            half_rev = half_rev.next
            head = head.next
        return True


# [1,4,-1,-1,4,1]
head1 = ListNode(1)
node12 = ListNode(2)
node13 = ListNode(-1)
# node14 = ListNode(-1)
node15 = ListNode(4)
node16 = ListNode(1)
head1.next = node12
node12.next = node13
node12.next = node13
node13.next = node15
node15.next = node16
node16.next = None

print(Solution().isPalindrome(head1))
