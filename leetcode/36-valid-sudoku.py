class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    x.extend([(i, board[i][j]), (board[i][j], j), (i // 3, j // 3, board[i][j])])
        return len(x) == len(set(x))