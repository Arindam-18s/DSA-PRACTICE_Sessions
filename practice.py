# 64. Minimum Path Sum - Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
                                                                # which minimizes the sum of all numbers along its path.
# -- Dynamic Programming Memoization Soln .
class Solution:                           #Tc -> O(n x m)   |   Sc -> O((n - 1)+(m - 1)) + O(n x m)
    def rec(self, i, j, grid, dp):
        if i == 0 and j == 0:
            return grid[i][j]
        if i < 0 or j < 0:
            return float('inf')
        if dp[i][j] != -1:
            return dp[i][j]
        up = grid[i][j] + self.rec(i - 1, j, grid, dp)
        left = grid[i][j] + self.rec(i, j - 1, grid, dp)
        dp[i][j] = min(up, left)
        return dp[i][j]
    
    def minPathSum(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        dp = [[-1 for _ in range(m)]for _ in range(n)]
        return self.rec(n - 1, m - 1, grid, dp)

# -- Dynamic Programming Tabulation Soln .
class Solution:                           #Tc -> O(n x m)   |   Sc -> O(n x m)
    def minPathSum(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                else:
                    up = dp[i - 1][j] if i > 0 else float('inf')
                    left = dp[i][j - 1] if j > 0 else float('inf')
                    
                    # Minimum of the two incoming paths + current cell cost
                    dp[i][j] = grid[i][j] + min(up, left)
        return dp[n - 1][m - 1]
                