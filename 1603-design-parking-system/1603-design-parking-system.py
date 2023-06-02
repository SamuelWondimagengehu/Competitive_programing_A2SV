class ParkingSystem:
    book = defaultdict(int)
    
    def __init__(self, big: int, medium: int, small: int):
        self.book[1] = big 
        self.book[2] = medium
        self.book[3] = small
        
    def addCar(self, carType: int) -> bool:
        if carType == 1:
            ans = (self.book[1] - 1) >= 0
            self.book[1] -= 1
        elif carType == 2:
            ans = (self.book[2] - 1) >= 0
            self.book[2] -= 1
        elif carType == 3:
            ans = (self.book[3] - 1) >= 0
            self.book[3] -= 1
        return ans


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)