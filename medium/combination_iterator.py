"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   12.04.2020 00:51
"""


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.__string = list(reversed(characters))
        self.__length = combinationLength
        self.__values = list(self.__helper_get_nums_length_bits())

    def get_value(self):
        return self.__values

    def __helper_get_nums_length_bits(self):
        cnt = 2 ** len(self.__string)
        dp = [0] * cnt
        dp[0] = 0
        dp[1] = 1
        for i in range(2, cnt):
            if (i & (i - 1)) == 0:
                dp[i] = 1
                continue
            if i % 2 == 0:
                dp[i] = dp[i >> 1]
            else:
                dp[i] = 1 + dp[i - 1]
        return reversed([i for i in range(cnt) if dp[i] == self.__length])

    def next(self) -> str:
        val = self.__values[0]
        self.__values.pop(0)
        result = ""
        for i in range(16, -1, -1):
            if val & (1 << i) and i < len(self.__string):
                result += self.__string[i]
        return result

    def hasNext(self) -> bool:
        return len(self.__values) > 0


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
obj = CombinationIterator("bvwz", 3)
print(obj.get_value())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())

