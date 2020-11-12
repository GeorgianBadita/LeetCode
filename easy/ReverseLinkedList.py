# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # if there is no node
        if not head:
            return head

        # if there's only one node
        if head.next is None:
            return head

        # if there are only two nodes
        if head.next.next is None:
            to_ret_head = head.next
            head.next.next = head
            head.next = None
            return to_ret_head

        # if there are at least three nodes
        cur_node = head.next.next
        last_node = head.next
        prev_last = head
        head.next = None
        while cur_node is not None:
            prev_curr = cur_node
            cur_node = cur_node.next
            last_node.next = prev_last
            prev_last = last_node
            last_node = prev_curr

        last_node.next = prev_last
        return last_node


ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
ll.next.next.next.next = ListNode(5)

rev_lst = Solution().reverseList(ll)

while rev_lst is not None:
    print(rev_lst.val)
    rev_lst = rev_lst.next
