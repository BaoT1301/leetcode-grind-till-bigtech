class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        self.perimeter = 0

        def dfs(r, c):
            
            if r >= row or c >= col or r < 0 or c < 0:
                self.perimeter += 1
                return
            elif grid[r][c] == 1:
                self.perimeter += 0
                grid[r][c] = "#"
            elif grid[r][c] == 0:
                self.perimeter += 1
                return
            else:
                return

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dfs(i, j)

        return self.perimeter

