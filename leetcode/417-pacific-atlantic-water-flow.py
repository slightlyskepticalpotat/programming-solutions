class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n, pacific, atlantic = len(heights), len(heights[0]), set(), set()
        def dfs(i, j, searched, last):
            if not -1 < i < m or not -1 < j < n or (i, j) in searched or heights[i][j] < last:
                return
            searched.add((i, j))
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(i + di, j + dj, searched, heights[i][j])
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, n - 1, atlantic, heights[i][n - 1])
        for j in range(n):
            dfs(0, j, pacific, heights[0][j])
            dfs(m - 1, j, atlantic, heights[m - 1][j])
        return [i for i in pacific if i in atlantic]