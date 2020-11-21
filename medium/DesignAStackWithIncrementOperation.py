# https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.__curr_size = 0
        self.__max_size = maxSize
        self.__stack = [None]*maxSize

    def push(self, x: int) -> None:
        if self.__curr_size < self.__max_size:
            self.__stack[self.__curr_size] = x
            self.__curr_size += 1

    def pop(self) -> int:
        if self.__curr_size == 0:
            return -1
        to_ret = self.__stack[self.__curr_size - 1]
        self.__curr_size -= 1
        return to_ret

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.__curr_size)):
            self.__stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)