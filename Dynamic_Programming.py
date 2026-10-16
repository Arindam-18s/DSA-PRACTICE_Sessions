# Fibonacci - Usage of Memoization DP (using Recursion Obv.) - O(n)

def fibo_using_memoization_dp(n, dp):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    return fibo_using_memoization_dp(n - 1, dp) + fibo_using_memoization_dp(n - 2, dp)

if __name__ == "__main__":
    n = 6
    dp = [-1] * (n + 1)
    print(fibo_using_memoization_dp(n, dp))

# --------------------------------------------------------------------------------------------------
# Fibonacci - Usage of Tabulation DP - O(n)

def fibo_using_Tabulation_dp(n, dp):
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

if __name__ == "__main__":
    n = 6
    dp = [-1] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    print(fibo_using_Tabulation_dp(n, dp))

# --------------------------------------------------------------------------------------------------
# 70. Climbing Stairs - Memoization DP | Time - O(n), Space - O(n)

class Solution:
    def rec(self, n, dp):
        if n <= 2:
            return n
        if dp[n] != -1:             #        <-- If Already Computed No need to compute again
            return dp[n]      
        dp[n] = self.rec(n - 1, dp) + self.rec(n - 2, dp)
        return dp[n]
    
    def climbStairs(self, n: int) -> int:
        if not n:
            return 0
        dp = [-1] * (n + 1)
        return self.rec(n, dp)
# --------------------------------------------------------------------------------------------------
# 198. House Robber - Memoization DP w Recursion - Time - O(n), Space - O(n)
                    # Maximum Sum of Non-Adjacent Elements
class Solution:
    def f(self, index, nums, dp):
        if index == 0:
            return nums[index]
        if index < 0:
            return 0
        if dp[index] != -1:
            return dp[index]

        pick = nums[index] + self.f(index - 2, nums, dp)
        not_pick = 0 + self.f(index - 1, nums, dp)
        dp[index] = max(pick, not_pick)
        return dp[index]

    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        dp = [-1] * len(nums)
        return self.f(len(nums) - 1, nums, dp)

# --------------------------------------------------------------------------------------------------
# 198. House Robber - Tabulation DP w Recursion - Time - O(n), Space - O(n)
                    # Maximum Sum of Non-Adjacent Elements
class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        for i in range(len(nums)):
            take = nums[i]
            if i > 1:
                take += dp[i - 2]
            not_take = 0 + dp[i - 1]
            dp[i] = max(take, not_take)
        return dp[len(nums) - 1]

# --------------------------------------------------------------------------------------------------
# 213. House Robber II- Memoization DP w Recursion - Time - O(n), Space - O(n)
                    # Maximum Sum of Non-Adjacent Elements - All houses at this place are arranged in a circle
class Solution:
    def f(self, index, nums, dp):
        if index == 0:
            return nums[index]
        if index < 1:
            return 0
        if dp[index] != -1:
            return dp[index]
        take = nums[index] + self.f(index - 2, nums, dp)
        not_take = 0 + self.f(index - 1, nums, dp)
        dp[index] = max(take, not_take)
        return dp[index]

    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        temp1 = []
        temp2 = []
        for i in range(len(nums)):
            if i != 0:
                temp1.append(nums[i])
            if i != len(nums) - 1:
                temp2.append(nums[i])

        dp1 = [-1] * len(temp1) 
        dp2 = [-1] * len(temp2)
        return max(self.f(len(temp1) - 1, temp1, dp1) , self.f(len(temp2) - 1, temp2, dp2))

# --------------------------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------------------------
# 63. Unique Paths II - Given an m x n integer array grid. There is a robot initially located at the top-left corner
                      # and tries to move to the bottom-right corner - An obstacle and space are marked as 1 or 0 
                      # in grid. A path that the robot takes cannot include any obstacle.
                      # Return the number of possible --unique paths--

class Solution:       # -- Dynamic Programming Memoization Soln .
    def rec(self, i, j, obstacleGrid, dp):
        if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
            return 0
        if i == 0 and j == 0:
            return 1
        if dp[i][j] != -1:
            return dp[i][j]
        up = self.rec(i - 1, j, obstacleGrid, dp)
        left = self.rec(i, j - 1, obstacleGrid, dp)
        dp[i][j] = up + left
        return dp[i][j]
    
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[n - 1][m - 1] == 1:
            return 0
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        return self.rec(n - 1, m - 1, obstacleGrid, dp)

# -- Dynamic Programming Tabulation Soln .
class Solution: 
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1 for _ in range(m)]for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    up = 0
                    left = 0
                    if i > 0:
                        up = dp[i - 1][j]
                    if j > 0:
                        left = dp[i][j - 1]
                    dp[i][j] = up + left
        return dp[n - 1][m - 1]

# --------------------------------------------------------------------------------------------------
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
                
# --------------------------------------------------------------------------------------------------
