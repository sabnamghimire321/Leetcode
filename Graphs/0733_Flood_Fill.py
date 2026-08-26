class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if old_color == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols):
                return
            if image[r][c] != old_color:
                return

            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
