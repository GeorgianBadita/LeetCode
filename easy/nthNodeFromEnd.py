"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   30.03.2020 21:17
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head

        tmp = head
        to_del = head
        for _ in range(n):
            tmp = tmp.next
        if tmp is None:
            to_del = to_del.next
            return to_del
        while tmp.next is not None:
            tmp = tmp.next
            to_del = to_del.next

        curr = to_del
        curr.next = to_del.next.next
        return head


nodes = [ListNode(x) for x in range(1, 6)]
head = nodes[0]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
nodes[-1].next = None

head = Solution().removeNthFromEnd(head, 2)

while head != None:
    print(head.val)
    head = head.next
