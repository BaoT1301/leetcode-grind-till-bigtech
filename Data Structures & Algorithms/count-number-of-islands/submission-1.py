class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        self.island = 0

        def dfs(r, c):

            if r >= row or c >= col or r < 0 or c < 0:
                return
            elif grid[r][c] == "0":
                return
            elif grid[r][c] == "1":
                grid[r][c] = "#"
                dfs(r + 1, c)
                dfs(r, c + 1)
                dfs(r - 1, c)
                dfs(r, c - 1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    self.island += 1
                    dfs(i, j)

        return self.island