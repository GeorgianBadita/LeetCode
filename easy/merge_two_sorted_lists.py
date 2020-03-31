"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   30.03.2020 23:26
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_begin(val, l):
    node = ListNode(val)
    node.next = l
    return node


def merge_lists_aux(l1, l2, col):
    if l1 is None and l2 is None:
        return col
    if l1 is None:
        return merge_lists_aux(l1, l2.next, add_begin(l2.val, col))
    if l2 is None:
        return merge_lists_aux(l1.next, l2, add_begin(l1.val, col))
    if l1.val <= l2.val:
        return merge_lists_aux(l1.next, l2, add_begin(l1.val, col))
    return merge_lists_aux(l1, l2.next, add_begin(l2.val, col))


def merge_lists(l1, l2):
    if l1.val <= l2.val:
        return merge_lists_aux(l1.next, l2, ListNode(l1.val))
    return merge_lists_aux(l1, l2.next, ListNode(l2.val))


def inv_list(head: ListNode) -> ListNode:
    if not head or head.next is None:
        return head
    first = head
    curr = head
    next = head.next
    while next is not None:
        curr1 = next
        next = next.next
        curr1.next = curr
        curr = curr1
    first.next = None
    return curr1


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l2:
            return l1
        if not l1:
            return l2
        return inv_list(merge_lists(l1, l2))


head1 = ListNode(1)
node12 = ListNode(2)
node13 = ListNode(4)
head1.next = node12
node12.next = node13
node13.next = None

head2 = ListNode(1)
node22 = ListNode(3)
node23 = ListNode(4)
head2.next = node22
node22.next = node23
node23.next = None

fin_list = Solution().mergeTwoLists(head1, head2)
while fin_list:
    print(fin_list.val)
    fin_list = fin_list.next
