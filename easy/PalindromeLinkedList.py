# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # if the list is empty or has only one node it's palindrome
        if not head or not head.next:
            return True

        # get list size
        size = 0
        head_cpy = head
        while head_cpy is not None:
            size += 1
            head_cpy = head_cpy.next

        # invert first half of the list
        prev = head
        curr = prev.next
        head.next = None
        for i in range(size // 2 - 1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        second_half_head = curr if size % 2 == 0 else curr.next
        while prev is not None:
            if prev.val != second_half_head.val:
                return False
            second_half_head = second_half_head.next
            prev = prev.next
        return True


ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(2)
ll.next.next.next = ListNode(3)
# ll.next.next.next.next = ListNode(1)

print(Solution().isPalindrome(ll))
