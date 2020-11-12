# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_list = ListNode()
        carry = 0
        l1_head = l1
        l2_head = l2
        res_list_head = result_list
        while l1_head != None and l2_head != None:
            curr_res = l1_head.val + l2_head.val + carry
            carry = curr_res // 10
            curr_res = curr_res % 10
            new_node = ListNode()
            new_node.val = curr_res
            res_list_head.next = new_node
            res_list_head = new_node
            l1_head = l1_head.next
            l2_head = l2_head.next

        while l1_head != None:
            curr_res = l1_head.val + carry
            carry = curr_res // 10
            curr_res = curr_res % 10
            new_node = ListNode()
            new_node.val = curr_res
            res_list_head.next = new_node
            res_list_head = new_node
            l1_head = l1_head.next

        while l2_head != None:
            curr_res = l2_head.val + carry
            carry = curr_res // 10
            curr_res = curr_res % 10
            new_node = ListNode()
            new_node.val = curr_res
            res_list_head.next = new_node
            res_list_head = new_node
            l2_head = l2_head.next

        if carry == 1:
            res_list_head.next = ListNode(1)

        return result_list.next
