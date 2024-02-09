class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0] * 1001
        last_stop = 0

        for trip in trips:
            passengers, init, dest = trip[0], trip[1], trip[2]

            stops[init] += passengers
            stops[dest] -= passengers

        curr_pass = 0

        for i in range(1001):
            curr_pass += stops[i]
            if curr_pass > capacity:
                return False
        
        return True        
        
