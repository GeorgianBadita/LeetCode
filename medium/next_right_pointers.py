"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   04.04.2020 22:33
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        tmp = root
        st = [tmp]
        while len(st) > 0:
            curr = st.pop()
            if curr.left:
                curr.left.next = curr.right
                st.append(curr.left)
            if curr.right:
                if curr.next:
                    curr.right.next = curr.next.left
                st.append(curr.right)

        return root
