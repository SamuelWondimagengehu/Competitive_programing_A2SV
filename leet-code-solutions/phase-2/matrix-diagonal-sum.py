class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat) == 1 and len(mat[0]) == 1:
            return sum(mat[0])
        
        directions = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
        
        x, y = 0, 0
        n, m = len(mat), len(mat[0])
        
        acc = 0
        while x < n and y < m:
            acc += mat[x][y]
            x += directions[0][0]
            y += directions[0][1]
        
        x, y = 0, m - 1
        while x < n and y >= 0:
            acc += mat[x][y]
            x += directions[3][0]
            y += directions[3][1]
        
        if len(mat) % 2 != 0:
            acc -= mat[n // 2][m // 2]
        else:
            return acc
        
        return acc
            
        
        