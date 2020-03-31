"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 23:08
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__min_val = None
        self.__elem_stack = []

    def push(self, x: int) -> None:
        if len(self.__elem_stack) == 0 or self.__min_val is None:
            self.__min_val = x
        if x <= self.__min_val:
            self.__min_val = x
        self.__elem_stack.append((x, self.__min_val))

    def pop(self) -> None:
        self.__elem_stack.pop()
        if len(self.__elem_stack) > 0:
            self.__min_val = self.__elem_stack[-1][1]
        else:
            self.__min_val = None

    def top(self) -> int:
        return self.__elem_stack[-1][0]

    def getMin(self) -> int:
        return self.__elem_stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
minStack.getMin()
