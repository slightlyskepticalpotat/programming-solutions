class Solution:
    def fill(self, i, j, grid):
        if not -1 < i < len(grid) or not -1 < j < len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "0"
        self.fill(i + 1, j, grid)
        self.fill(i - 1, j, grid)
        self.fill(i, j + 1, grid)
        self.fill(i, j - 1, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # use dfs to fill in the connected waters
                    self.fill(i, j, grid)
                    ans += 1
        return ans