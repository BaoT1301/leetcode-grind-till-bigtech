class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        self.perimeter = 0

        def dfs(r, c):
            
            if r >= row or r < 0 or c >= col or c < 0:
                self.perimeter += 1
                return

            elif grid[r][c] == 1:
                grid[r][c] = "#"
            elif grid[r][c] == 0:
                self.perimeter += 1
                return
            elif grid[r][c] == "#":
                return

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    dfs(r, c)

        return self.perimeter