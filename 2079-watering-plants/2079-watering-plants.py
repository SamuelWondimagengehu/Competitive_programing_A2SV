class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        river_store = capacity
        ans = 0
        
        for i, val in enumerate(plants):
            if capacity >= val:
                capacity -= val
                ans += 1
            else:
                ans += i + (i + 1)
                capacity = river_store - val
                
        return ans
                
        