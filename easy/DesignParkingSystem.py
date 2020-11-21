# https://leetcode.com/problemset/algorithms/?difficulty=Easy&status=Todo

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.__big = big
        self.__medium = medium
        self.__small = small        

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.__big > 0:
            self.__big -= 1
            return True
        if carType == 2 and self.__medium > 0:
            self.__medium -= 1
            return True
        if carType == 3 and self.__small > 0:
            self.__small -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)