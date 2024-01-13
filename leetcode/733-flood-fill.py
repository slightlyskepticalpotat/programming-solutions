class Solution:
    def floodFill(self, image, sr, sc, color):
        old = image[sr][sc]
        visited = set()
        def dfs(i, j):
            if not (-1 < i < len(image)) or not (-1 < j < len(image[0])) or image[i][j] != old or (i, j) in visited:
                return
            visited.add((i, j))
            image[i][j] = color
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        dfs(sr, sc)
        return image
