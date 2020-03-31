"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   30.03.2020 23:15
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_list_begin(lst, val):
    node = ListNode(val)
    node.next = lst
    return node


def rev_lst_aux(lst, col):
    if lst is None:
        return col
    return rev_lst_aux(lst.next, add_list_begin(col, lst.val))


class SolutionRec:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        return rev_lst_aux(head.next, ListNode(head.val))


class SolutionIter:
    def reverseList(self, head: ListNode) -> ListNode:
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


nodes = [ListNode(x) for x in range(1, 6)]
head = nodes[0]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
nodes[-1].next = None

head = SolutionIter().reverseList(head)

while head is not None:
    print(head.val)
    head = head.next
