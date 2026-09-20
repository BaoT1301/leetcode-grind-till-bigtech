class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        self.maxCount = 0
        self.count = 0

        def dfs(r, c):
            count = 0
            if r >= row or r < 0 or c >= col or c < 0:
                return 0
            elif grid[r][c] == 1:
                count += 1
                grid[r][c] = "#"

                count += dfs(r + 1, c)
                count += dfs(r - 1, c)
                count += dfs(r, c + 1)
                count += dfs(r, c - 1)

                self.maxCount = max(self.maxCount, count)

            else:
                return 0

            return count

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    dfs(r, c)

        return self.maxCount
            