class Solution:
    def transpose(self, mat: List[List[int]]) -> List[List[int]]:
        cols = len(mat)
        rows = len(mat[0])
        grid = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = mat[j][i]

        return grid