class Robot:

    def __init__(self, width: int, height: int):
        self.x = 0
        self.y = 0
        self.w = width
        self.h = height
        self.dir = 0
        self.dlabels = ["East", "North", "West", "South"]
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
    def step(self, num: int) -> None:
        def is_valid(x, y):
            return 0 <= x < self.w and 0 <= y < self.h
        
        num %= (self.w - 1 + self.h - 1) * 2
        
        if num == 0:
            num += (self.w - 1 + self.h - 1) * 2
        
        for _ in range(num):
            xn, yn = self.x + self.directions[self.dir][0], self.y + self.directions[self.dir][1]
            
            while not is_valid(xn, yn):
                self.dir = (self.dir + 1) % 4
                xn, yn = self.x + self.directions[self.dir][0], self.y + self.directions[self.dir][1]
            
            self.x = xn
            self.y = yn
        
    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.dlabels[self.dir]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()