class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
     
        def backtrack(r, c, i):
            if i == len(word):
                return True
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[i]:
                return False
     
            temp = board[r][c]
            board[r][c] = '#'  
            found = any(backtrack(r+dr, c+dc, i+1) for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)))
            board[r][c] = temp  
     
            return found
     
        return any(backtrack(r, c, 0) for r in range(rows) for c in range(cols))
