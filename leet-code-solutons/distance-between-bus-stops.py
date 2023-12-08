class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total_distance, clockwise_distance = 0, 0
        
        for i, d in enumerate(distance):
            if start < destination and (start <= i and destination > i):
                clockwise_distance += d
                
            if start > destination and (start <= i or destination > i):
                clockwise_distance += d
            
            total_distance += d
        
        return min(clockwise_distance, total_distance - clockwise_distance)