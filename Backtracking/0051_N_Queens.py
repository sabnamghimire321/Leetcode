class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        cols, diag1, diag2 = set(), set(), set()
        placement = []
 
        def backtrack(row):
            if row == n:
                board = ["." * c + "Q" + "." * (n - c - 1) for c in placement]
                solutions.append(board)
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col); diag1.add(row - col); diag2.add(row + col)
                placement.append(col)
     
                backtrack(row + 1)
     
                cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)
                placement.pop()
     
        backtrack(0)
        return solutions
