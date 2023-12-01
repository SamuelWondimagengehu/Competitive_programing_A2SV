class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix) - 1
        col = len(matrix[0]) - 1

        for j in range(row):
            for i in range(col):
                if i + 1 <= col and j + 1 <= row and matrix[j][i] != matrix[j + 1][i + 1]:
                    return False
        
        return True
