class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []
 
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.append((r, c))
                else:
                    d = board[r][c]
                    rows[r].add(d); cols[c].add(d); boxes[(r//3)*3 + c//3].add(d)
 
        def backtrack(k):
            if k == len(empties):
                return True
            r, c = empties[k]
            b = (r//3)*3 + c//3
            for digit in '123456789':
                if digit in rows[r] or digit in cols[c] or digit in boxes[b]:
                    continue
                rows[r].add(digit); cols[c].add(digit); boxes[b].add(digit)
                board[r][c] = digit
 
                if backtrack(k + 1):
                    return True
 
                rows[r].remove(digit); cols[c].remove(digit); boxes[b].remove(digit)
                board[r][c] = '.'
            return False
 
        backtrack(0)
