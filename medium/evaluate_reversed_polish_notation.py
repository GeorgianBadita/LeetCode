"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   10.04.2020 23:48
"""
import math
from typing import List


class Solution:

    def get_op(self, op):
        if op == '+':
            return lambda x, y: x + y
        if op == '-':
            return lambda x, y: x - y
        if op == '*':
            return lambda x, y: x * y
        if op == '/':
            return lambda x, y: int(x / y)
        return None

    def evalRPN(self, tokens: List[str]) -> int:
        op_stack = []
        for token in tokens:
            if token in "+-*/":
                op1 = op_stack.pop()
                op2 = op_stack.pop()
                function = self.get_op(token)
                op_stack.append(function(op2, op1))
            else:
                op_stack.append(int(token))
        return op_stack[0]


print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
