# 62. Unique Paths - There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
                   # The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move 
                   # either down or right at any point in time. Given the two integers m and n, return the number of possible 
                   # unique paths that the robot can take to reach the bottom-right corner.
# -- Recursive Soln.
                    #Tc -> O(2 ^ (n + m))   |   Sc -> O((n - 1)+(m - 1)) - ***Gets TLE 100%***
class Solution:
    def recursion(self, i, j):
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0
        up = self.recursion(i - 1, j)
        left = self.recursion(i, j - 1)
        return up + left
    def uniquePaths(self, m: int, n: int) -> int:
        return self.recursion(m - 1, n - 1)
    
# -- Dynamic Programming Memoization Soln .
                    #Tc -> O(n x m)   |   Sc -> O((n - 1)+(m - 1)) + O(n x m)
class Solution:
    def recursion(self, i, j, dp):
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        up = self.recursion(i - 1, j, dp)
        left = self.recursion(i, j - 1, dp)
        dp[i][j] = up + left
        return dp[i][j]
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.recursion(m - 1, n - 1, dp)

# -- Dynamic Programming Tabulation Soln .
                    #Tc -> O(n x m)   |   Sc -> O(n x m)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)]for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                up = 0
                left = 0
                if i > 0:
                    up = dp[i - 1][j]
                if j > 0:
                    left = dp[i][j - 1]
                dp[i][j] = up + left
        return dp[m - 1][n - 1]