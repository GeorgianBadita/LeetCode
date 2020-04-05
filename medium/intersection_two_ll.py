"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   01.04.2020 22:59
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        first, second = headA, headB

        while first != second:
            first = first.next if first else headB
            second = second.next if second else headA

        return first
