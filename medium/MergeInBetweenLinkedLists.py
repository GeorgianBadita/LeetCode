# https://leetcode.com/submissions/detail/427432636/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:

        head_a = list1
        diff = b - a

        while a - 1 > 0:
            head_a = head_a.next
            a -= 1

        head_b = head_a.next
        while diff > 0:
            head_b = head_b.next
            diff -= 1
        head_b = head_b.next
        final_node_list2 = list2
        while final_node_list2.next != None:
            final_node_list2 = final_node_list2.next

        head_a.next = list2
        final_node_list2.next = head_b
        return list1