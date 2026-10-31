from typing import List
class Solution:
    MOD = (10 ** 9) + 7
    def rec(self, i, j, d,grid, dp):
        if i < 0 or j < 0:             # Base Cases: Out of bounds
            return 0
        if i == 0 and j == 0:          # Base Case: Reached starting cell (0, 0)
            if grid[0][0] == 1:
                return 0
            return 1
        if dp[i][j][d] != -1:          # Check 3D memoization table: dp[i][j][d]
            return dp[i][j][d]
        if grid[i][j] == 1:
            if d == 0:
                ans = self.rec(i, j - 1, 1, grid, dp)
            else:
                ans = self.rec(i - 1, j, 0, grid, dp)
        else:
            up = self.rec(i - 1, j, 0, grid, dp)
            left = self.rec(i, j - 1, 1, grid, dp)
            ans = (up + left) % self.MOD
        dp[i][j][d] = ans
        return dp[i][j][d]

    def uniquePaths(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[[-1, -1] for _ in range(m)]for _ in range(n)]  # 3D DP : dp[n][m][2] 3rd dim tracks direction

        from_top = self.rec(n - 1, m - 1, 0, grid, dp)
        from_left = self.rec(n - 1, m - 1, 1, grid, dp)
        total_paths = (from_top + from_left) % self.MOD
        
        inv_2 = (self.MOD + 1) // 2                          # Multiply by modular inverse of 2 to divide under MOD
        return (total_paths * inv_2) % self.MOD