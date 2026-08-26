class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n):
            is_pal[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or is_pal[i+1][j-1]):
                    is_pal[i][j] = True
     
        cuts = [0] * n
        for j in range(n):
            if is_pal[0][j]:
                cuts[j] = 0
                continue
            cuts[j] = min(cuts[i-1] + 1 for i in range(1, j+1) if is_pal[i][j])
     
        return cuts[n-1]
