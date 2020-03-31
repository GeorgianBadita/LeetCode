"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   30.03.2020 21:08
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        next = node.next
        node.val = node.next.val
        node.next = next.next

lst = ListNode(4)
del_node = ListNode(5)
node2 = ListNode(1)
node3 = ListNode(9)
lst.next = del_node
del_node.next = node2
node2.next = node3
Solution().deleteNode(node2)
while lst != None:
    print(lst.val)
    lst = lst.next