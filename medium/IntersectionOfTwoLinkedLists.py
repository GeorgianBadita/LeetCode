# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/785/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        l1 = headA
        l2 = headB

        while l1 != l2:
            l1 = l1.next if l1 is not None else headB
            l2 = l2.next if l2 is not None else headA

        return l1

print("caca")