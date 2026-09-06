class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        maxLength = 0

        def dfs(r, c):
            area = 0
            if r >= row or c >= col or r < 0 or c < 0:
                return 0
            elif grid[r][c] == 1:
                area += 1
                grid[r][c] = "#"
                area += dfs(r + 1, c)
                area += dfs(r , c + 1)
                area += dfs(r - 1, c)
                area +=dfs(r, c - 1)
            elif grid[r][c] == 0:
                return 0

            return area

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    max1 = dfs(i, j)
                    maxLength = max(max1, maxLength)

        return maxLength


        

