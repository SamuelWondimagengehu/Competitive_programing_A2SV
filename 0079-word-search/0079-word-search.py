class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, i):
            #If word pointer manages to reach the end without 
            #the conditions failing in the middle: return True
            if i == len(word): 
                return True
            
            #if the board pointers go out of bound, or word[i] not equals board[r][c]
            #or we're already on a path that has been visited: return False
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path
            ):
                return False
            
            path.add((r, c))
            
            #explore in all four directions
            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            
            path.remove((r, c))
            
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0): return True
        
        return False