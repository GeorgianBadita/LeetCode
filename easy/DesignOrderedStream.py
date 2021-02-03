# https://leetcode.com/problems/design-an-ordered-stream/submissions/


from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.__list = [None]*n
        self.__ptr = 0

    def __all_printed(self, i):
        for i in range(i):
            if self.__list[i] is None:
                return False
        return True

    def insert(self, id: int, value: str) -> List[str]:
        self.__list[id - 1] = value

        curr_ptr = self.__ptr
        while self.__ptr < len(self.__list) and self.__list[self.__ptr]:
            self.__ptr += 1

        return self.__list[curr_ptr:self.__ptr]

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
