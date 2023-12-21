class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return None

        m, n = len(mat), len(mat[0])

        ans = [[] for _ in range(n + m - 1)]

        for i in range(m):
            for j in range(n):
                ans[i + j].append(mat[i][j])
        
        result = []
        for i in range(len(ans)):
            if i % 2 == 0:
                result.extend(ans[i][::-1])
            else:
                result.extend(ans[i])
        
        return result