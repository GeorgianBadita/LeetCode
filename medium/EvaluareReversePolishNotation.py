# https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/823/

from typing import List


class Solution:

    def __init__(self) -> None:
        self.__operators = "+-*/"

    def apply_operator(self, op1, op, op2):
        if op == '+':
            return op1 + op2

        if op == '-':
            return op1 - op2

        if op == '/':
            return int(op1 / op2)

        if op == '*':
            return op1 * op2

    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        operands_stack = []

        for token in tokens:
            if token in self.__operators:
                op2 = operands_stack.pop()
                op1 = operands_stack.pop()
                operands_stack.append(self.apply_operator(op1, token, op2))
            else:
                operands_stack.append(int(token))

        return operands_stack.pop()


print(Solution().evalRPN(["10", "6", "9", "3", "+",
                          "-11", "*", "/", "*", "17", "+", "5", "+"]))
