class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        def dfs(r, c):

            if r >= row or r < 0 or c >= col or c < 0:
                return
            if grid[r][c] == "1":
                grid[r][c] = "#"

                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r , c + 1)
                dfs(r, c - 1)
            else:
                return

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count

        