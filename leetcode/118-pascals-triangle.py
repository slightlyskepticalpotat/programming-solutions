class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return pascal if (pascal := [[1]]) and pascal.extend([1] + [pascal[i][j] + pascal[i][j + 1] for j in range(i)] + [1] for i in range(numRows - 1)) else pascal