# https://leetcode.com/explore/interview/card/top-interview-questions-medium/112/design/811/

from typing import List


class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.__vector = v
        self.__x = 0
        self.__y = 0

    def __skip_empty(self):
        while self.__x < len(self.__vector) and len(self.__vector[self.__x]) == 0:
            self.__x += 1

    def next(self) -> int:
        self.__skip_empty()
        to_return = self.__vector[self.__x][self.__y]
        self.__y += 1
        if self.__y == len(self.__vector[self.__x]):
            self.__x += 1
            self.__y = 0
        return to_return

    def hasNext(self) -> bool:
        if len(self.__vector) == 0:
            return False
        self.__skip_empty()
        if self.__x == len(self.__vector):
            return False

        if self.__x < len(self.__vector) - 1:
            return True
        return self.__y < len(self.__vector[self.__x])


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
