# 867. Transpose Matrix - Given a 2D integer array matrix, return the transpose of matrix.
                      # The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

class Solution:                # Time -> 0(R x C), Space -> O(R x C)
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        row, column = len(matrix), len(matrix[0])
        Transposed = [[0 for _ in range(row)]for _ in range(column)]
        for i in range(row):
            for j in range(column):
                Transposed[j][i] = matrix[i][j]
        return Transposed

