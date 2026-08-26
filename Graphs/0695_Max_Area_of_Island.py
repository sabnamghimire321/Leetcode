class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols):
                return 0
            if visited[r][c]:
                return 0
            if grid[r][c] != 1:
                return 0

            visited[r][c] = True

            return (
                1
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )

        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    best = max(best, dfs(r, c))

        return best
