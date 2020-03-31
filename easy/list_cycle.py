"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 00:00
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next or not head.next.next or not head.next.next.next:
            return False

        tortoise = head
        hare = head.next.next
        while tortoise is not None:
            if hare.next and hare.next.next:
                hare = hare.next.next
            else:
                return False
            tortoise = tortoise.next

            if hare == tortoise:
                return True
        return False


head = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = None

print(Solution().hasCycle(head))