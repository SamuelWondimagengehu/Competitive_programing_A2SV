class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        p1 = points[0]
        
        for i in range(1, len(points)):
            p2 = points[i]
            px, py = p1[0] - p2[0], p1[1] - p2[1]
            count += max(abs(px), abs(py))
            p1 = p2
        
        return count
            