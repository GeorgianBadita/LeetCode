import abc
from abc import ABC, abstractmethod

from typing import List

"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node(ABC):

    def __init__(self, value, left=None, right=None) -> None:
        self._value = value
        self._left = left
        self._right = right

    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class OperandNode(Node):
    def __init__(self, value, left=None, right=None) -> None:
        super().__init__(value, left, right)

    def evaluate(self) -> int:
        return int(self._value)


class OperatorNode(Node):
    def __init__(self, value, left=None, right=None) -> None:
        super().__init__(value, left, right)

    def apply_op(self, op1, op, op2):
        if op == '+':
            return op1 + op2
        if op == '-':
            return op1 - op2
        if op == '*':
            return op1 * op2
        return int(op1 / op2)

    def evaluate(self) -> int:
        return self.apply_op(self._left.evaluate(), self._value, self._right.evaluate())

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for token in postfix:
            if token not in "/-*+":
                stack.append(OperandNode(token))
            else:
                op2_node = stack.pop()
                op = token
                op1_node = stack.pop()
                stack.append(OperatorNode(op, op1_node, op2_node))
        
        return stack.pop()

print(TreeBuilder().buildTree(["4","5","7","2","+","-","*"]).evaluate())

