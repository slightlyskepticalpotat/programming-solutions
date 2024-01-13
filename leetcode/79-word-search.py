class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board, self.word = board, word
        return any(self.dfs(i, j, 0) for i in range(len(board)) for j in range(len(board[0])))
    def dfs(self, i, j, k):
        if not self.board[i][j] == self.word[k]: # if letter doesn't match
            return False
        if len(self.word) == k + 1: # we found the word
            return True
        self.board[i][j] = "."
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if not (-1 < x < len(self.board) and -1 < y < len(self.board[0])):
                continue
            if self.dfs(x, y, k + 1): # if next find word
                return True
        self.board[i][j] = self.word[k]
        return False