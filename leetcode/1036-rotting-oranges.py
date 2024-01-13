class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n, time = len(grid), len(grid[0]), 0
        rot = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1}
        while fresh:
            if not rot:
                return -1
            rot = {(i + dx, j + dy) for i, j in rot for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (i + dx, j + dy) in fresh}
            fresh, time = fresh - rot, time + 1
        return time