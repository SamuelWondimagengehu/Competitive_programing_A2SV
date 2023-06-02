class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            ans = (self.big - 1) >= 0
            self.big -= 1
        elif carType == 2:
            ans = (self.medium - 1) >= 0
            self.medium -= 1
        elif carType == 3:
            ans = (self.small - 1) >= 0
            self.small -= 1
        return ans


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)