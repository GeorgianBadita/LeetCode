"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   10.04.2020 22:01
"""

from random import randint, choice


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__prime = 1747
        self.__set = [[] for _ in range(self.__prime)]

    def __search(self, n):
        hash_key = n % self.__prime
        return n in self.__set[hash_key]

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if not self.__search(val):
            self.__set[val % self.__prime].append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        try:
            self.__set[val % self.__prime].remove(val)
            return True
        except ValueError:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        candidates = [x for x in range(self.__prime) if len(self.__set[x]) > 0]
        random_hash = choice(candidates)
        len_hash = len(self.__set[random_hash])
        random_ind = randint(0, len_hash - 1)
        return self.__set[random_hash][random_ind]


# Your RandomizedSet object will be instantiated and called as such:
randomSet = RandomizedSet()

# Inserts 1 to the set. Returns true as 1 was inserted successfully.
print(randomSet.insert(1))

# Returns false as 2 does not exist in the set.
print(randomSet.remove(2))

# Inserts 2 to the set, returns true. Set now contains [1,2].
print(randomSet.insert(2))

# getRandom should return either 1 or 2 randomly.
print(randomSet.getRandom())

# Removes 1 from the set, returns true. Set now contains [2].
print(randomSet.remove(1))

# 2 was already in the set, so return false.
print(randomSet.insert(2))

# Since 2 is the only number in the set, getRandom always return 2.
print(randomSet.getRandom())
