class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        ans, r_begin, c_begin, r_end, c_end = [], 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        while r_begin <= r_end and c_begin <= c_end:
            ans.extend(matrix[r_begin][i] for i in range(c_begin, c_end + 1)) # equivalent of for loop with appends
            r_begin += 1
            ans.extend(matrix[i][c_end] for i in range(r_begin, r_end + 1))
            c_end -= 1
            if (r_begin <= r_end):
                ans.extend(matrix[r_end][i] for i in range(c_end, c_begin - 1, -1))
                r_end -= 1
            if (c_begin <= c_end):
                ans.extend(matrix[i][c_begin] for i in range(r_end, r_begin - 1, -1))
                c_begin += 1
        return ans