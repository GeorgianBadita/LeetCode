# https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return ''.join([x if x != '.' else '[.]' for x in address])
