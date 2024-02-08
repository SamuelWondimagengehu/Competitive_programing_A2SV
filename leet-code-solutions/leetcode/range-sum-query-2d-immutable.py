class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.pref_sum_mat = None
        else:
            rows, cols = len(matrix), len(matrix[0])
            self.pref_sum_mat = [[0] * (cols + 1) for _ in range(rows + 1)]

            # Build the cumulative sum matrix
            for i in range(1, rows + 1):
                for j in range(1, cols + 1):
                    self.pref_sum_mat[i][j] = matrix[i - 1][j - 1] + \
                                                       self.pref_sum_mat[i - 1][j] + \
                                                       self.pref_sum_mat[i][j - 1] - \
                                                       self.pref_sum_mat[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.pref_sum_mat:
            return 0

        return self.pref_sum_mat[row2 + 1][col2 + 1] - \
               self.pref_sum_mat[row1][col2 + 1] - \
               self.pref_sum_mat[row2 + 1][col1] + \
               self.pref_sum_mat[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)