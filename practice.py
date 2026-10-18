# PROBLEM - Maximum Falling Path Sum - Given an n x n array of integers matrix, 
                                     # return the maximum sum of any falling path through matrix.
# -- Dynamic Programming Memoization Soln. Tcol -> O(n x n)  |  Scol -> O(n x n) + O(n) 
class Solution:
    def rec_memoization(self, i, j, Matrix_Array, dp):
        if j < 0 or j >= len(Matrix_Array[0]):    # Out of bounds Base Case check using Matrix_Array width (m)
            return float('-inf')
        if i == 0:                          # Destination Base Case
            return Matrix_Array[0][j]
        if dp[i][j] != float('-inf'):
            return dp[i][j]

        up = Matrix_Array[i][j] + self.rec_memoization(i - 1, j , Matrix_Array, dp)
        left_diagonal = Matrix_Array[i][j] + self.rec_memoization(i - 1, j - 1, Matrix_Array, dp)
        right_diagonal = Matrix_Array[i][j] + self.rec_memoization(i - 1, j + 1, Matrix_Array, dp)
        dp[i][j] = max(up, left_diagonal, right_diagonal)
        return dp[i][j]

    def maxFallingPathSum(self, Matrix_Array, n, m):
        dp = [[float('-inf') for _ in range(m)]for _ in range(n)]
        maximum_sum = float('-inf')
        for j in range(m):
            maximum_sum = max(maximum_sum, self.rec_memoization(n - 1, j, Matrix_Array, dp))
        return maximum_sum

# -- Dynamic Programming Tabulation Soln. Tcol -> O(n x n) + O(n) |  Scol -> O(n x n)
    def maxFallingPathSum_using_Tabulation(self, Matrix_Array, n, m):
        dp = [[float('-inf') for _ in range(m)]for _ in range(n)]
        for j in range(m):
            dp[0][j] = Matrix_Array[0][j]

        for i in range(1, n):
            for j in range(m):
                up = Matrix_Array[i][j] + dp[i - 1][j]
                left_diagonal = float('-inf')
                if (j - 1) >= 0:
                    left_diagonal = Matrix_Array[i][j] + dp[i - 1][j - 1]
                right_diagonal = float('-inf')
                if (j + 1) < m:
                    right_diagonal = Matrix_Array[i][j] + dp[i - 1][j + 1]  
                dp[i][j] = max(up, left_diagonal, right_diagonal)  

        maximum_sum = dp[n - 1][0]
        for j in range(m):
            maximum_sum = max(maximum_sum, dp[n - 1][j])
        return maximum_sum

Matrix_Array = [[2,1,3],[6,5,4],[7,8,9]]
n, m = len(Matrix_Array), len(Matrix_Array[0])
sol = Solution()
# print(sol.maxFallingPathSum(Matrix_Array, n, m))
# print(sol.maxFallingPathSum_using_Tabulation(Matrix_Array, n, m))


# 931. - Minimum Falling Path Sum - Given an n x n array of integers matrix, 
                                     # return the minimum sum of any falling path through matrix.
# -- Dynamic Programming Memoization Soln. Tcol -> O(n x n)  |  Scol -> O(n x n) + O(n) 
class Solution:
    def rec(self, i, j, matrix, dp):
        if j < 0 or j >= len(matrix[0]):
            return float('inf')
        if i == 0:
            return matrix[0][j]
        if dp[i][j] != float('inf'):
            return dp[i][j]
        
        up = matrix[i][j] + self.rec(i - 1, j, matrix, dp)
        left_diagonal = matrix[i][j] + self.rec(i - 1, j - 1, matrix, dp)
        right_diagonal = matrix[i][j] + self.rec(i - 1, j + 1, matrix, dp)
        dp[i][j] = min(up, left_diagonal, right_diagonal)
        return dp[i][j]    
        
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[float('inf') for _ in range(m)]for _ in range(n)]
        minimum_sum = float('inf')
        for j in range(m):
            minimum_sum = min(minimum_sum, self.rec(n - 1, j, matrix, dp))
        return minimum_sum

# -- Dynamic Programming Tabulation Soln. Tcol -> O(n x n) + O(n) |  Scol -> O(n x n)
    def minFallingPathSum_using_Tabulation(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[float('inf') for _ in range(m)]for _ in range(n)]
        for j in range(m):
            dp[0][j] = matrix[0][j]
        
        for i in range(1, n):
            for j in range(m):
                up = matrix[i][j] + dp[i - 1][j]
                left_diagonal = float('inf')
                if j - 1 >= 0:
                    left_diagonal = matrix[i][j] + dp[i - 1][j - 1]
                right_diagonal = float('inf')
                if j + 1 < m:
                    right_diagonal = matrix[i][j] + dp[i - 1][j + 1]
                dp[i][j] = min(up, left_diagonal, right_diagonal)
        minimum_sum = float('inf')
        for j in range(m):
            minimum_sum = min(minimum_sum, dp[n - 1][j])
        return minimum_sum