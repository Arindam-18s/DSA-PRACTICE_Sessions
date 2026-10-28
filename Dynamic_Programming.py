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
# 120. Triangle --- Given a triangle array, return the minimum path sum from top to bottom.
                    # EX - Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]  - Output: 11
                    # -- Dynamic Programming Memoization Soln. Tcol -> O(n x n)  |  Scol -> O(n x n) + O(n)
class Solution:     
    def rec(self, i, j, triangle, dp):
        if i == (len(triangle) - 1):                                               #    2
            return triangle[len(triangle) - 1][j]                                  #   3 4
        if dp[i][j] is not None:                                                   #  6 5 7
            return dp[i][j]                                                        # 4 1 8 3
        down = triangle[i][j] + self.rec(i + 1, j, triangle, dp)
        diagonal = triangle[i][j] + self.rec(i + 1, j + 1, triangle, dp)
        dp[i][j] = min(down, diagonal)
        return dp[i][j]
    
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if not triangle:
            return 0
        n = len(triangle)
        dp = [[None for _ in range(n)]for _ in range(n)]
        return self.rec(0, 0, triangle, dp)

class Solution:      # -- Dynamic Programming Tabukation Soln. Tcol -> O(n x n)  |  Scol -> O(n x n)
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        dp = [[-1 for _ in range(n)]for _ in range(n)]

        # Fill the bottom row of dp with the actual bottom row of the triangle
        for j in range(n):
            dp[n - 1][j] = triangle[n - 1][j]

        for i in range(n - 2, -1, -1):
            for j in range(i, -1 , -1):
                down = triangle[i][j] + dp[i + 1][j]
                diagonal = triangle[i][j] + dp[i + 1][j + 1]
                dp[i][j] = min(down,diagonal)
        return dp[0][0]

# --------------------------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------------------------
            # ***  DP on SubSet, SubSequences And Target  ***
# --------------------------------------------------------------------------------------------------
# PROBLEM - Subset Sum Equals K - Given an Array and K, return True if there Exist any subset of that array, that sums up to K
#                                                  -- Dynamic Programming Memoization Soln. --
def subset_sum_equals_k_Dp_Memoization(index, target, array):   # Tcol -> O(n x n)  |  Scol -> O(n x n) + O(n) 
    if target == 0:
        return True
    if index < 0:
        return False
    if index == 0:
        if array[index] == target:
            return True
    if dp[index][target] != -1:
        return dp[index][target]
    not_take = subset_sum_equals_k_Dp_Memoization(index - 1, target, array)
    take = False
    if target >= array[index]:
        not_take = subset_sum_equals_k_Dp_Memoization(index - 1, target - array[index], array)

    dp[index][target] = take or not_take
    return dp[index][target]

if __name__ == "__main__":
    array = [1, 3, 2, 4]
    k = 11
    # Initialize a 2D list with -1 of size (n) x (k + 1)
    # Rows represent the index (0 to n-1), Columns represent the target (0 to k)
    dp = [[-1 for _ in range(k + 1)] for _ in range(len(array))]
    print(subset_sum_equals_k_Dp_Memoization(len(array) - 1, k, array))

    # ---*--- Dynamic Programming Tabulation Soln. ---*---       
if __name__ == "__main__":      # Tcol -> O(n x n)  |  Scol -> O(n x n) + O(n)
    array = [1, 3, 2, 4]
    k = 5
    dp = [[False for _ in range(k + 1)] for _ in range(len(array))]
    for i in range(len(array)):
        dp[i][0] = True
    if array[0] <= k:
        dp[0][array[0]] = True  

    for index in range(1, len(array)):
        for target in range(1, k + 1):
            not_take = dp[index - 1][target]
            take = False
            if target >= array[index]:
                take = dp[index - 1][target - array[index]]
            dp[index][target] = take | not_take
    print(dp[len(array) - 1][k])

# --------------------------------------------------------------------------------------------------
# 416. Partition Equal Subset Sum - Given an integer array nums, return true if you can partition the array 
#           into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
                                        # ---*--- Dynamic Programming Tabulation Soln. ---*---       
def subset_sum_eq_K_Tabulation(array, k):       # Tcol -> O(n x k)  |  Scol -> O(n x k)
    dp = [[False for _ in range(k + 1)] for _ in range(len(array))]
    for i in range(len(array)):       # Base case: a target sum of 0 is always possible (with an empty subset)
        dp[i][0] = True
    if array[0] <= k:                 # Base case: for the first element
        dp[0][array[0]] = True

    for index in range(1, len(array)):
        for target in range(1, k + 1):
            not_take = dp[index - 1][target]
            take = False
            if target >= array[index]:
                take = dp[index - 1][target - array[index]]
            dp[index][target] = take | not_take
    return dp[len(array) - 1][k]

if __name__ == "__main__":
    array = [1, 5, 11, 5]
    total_sum = sum(array)

    if total_sum % 2 != 0:      # If the total sum is odd, we cannot partition it into two equal integer sums
        print(False)
    else:
        target = total_sum // 2
        print(subset_sum_eq_K_Tabulation(array, target))

# --------------------------------------------------------------------------------------------------
# 2035. Partition Array Into Two Arrays to Minimize Sum Difference - You need to partition nums into 
# two arrays of length n to minimize the absolute difference of the sums of the arrays.Return the 
                                                            # minimum possible absolute difference.
class Solution:                     # ---*--- Dynamic Programming Tabulation Soln. ---*---  
    def minimumDifference(self, nums: list[int]) -> int:
        total_sum = sum(nums)       # Tcol -> O(n x k)  |  Scol -> O(n x k)
        k = total_sum
        
        dp = [[False for _ in range(k + 1)]for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True
        if nums[0] <= k:
            dp[0][nums[0]] = True
        for index in range(1, len(nums)):
            for target in range(1, k + 1):
                not_take = dp[index - 1][target]
                take = False
                if nums[index] <= target:
                    take = dp[index - 1][target - nums[index]]
                dp[index][target] = take or not_take

        # dp[n - 1][col 0 ->.....total_Sum]
        min_difference = float('inf')
        for s1 in range((total_sum // 2) + 1):
            if dp[len(nums) - 1][s1] == True:
                min_difference = min(min_difference, (total_sum - s1) - s1) 
        return min_difference

sol = Solution()
# print(sol.minimumDifference([3,9,7,3]))

# --------------------------------------------------------------------------------------------------
# PROBLEM - Count Subsets with Sum K | Given an array arr[] of non-negative integers and an integer target, 
# count all subsets of the array whose sum is equal to the given target. Input: arr[] = [5, 2, 3, 10, 6, 8], target = 10
                            # Explanation: The subsets {5, 2, 3}, {2, 8}, and {10} sum up to the target 10.   Output: 3
                            # -- Dynamic Programming Memoization Soln. -- 
class Solution:                             # • Time Col: (N x target); Space Col: (N x target);
    def func(self, index, target, array, dp):       
        if index == 0:                                      # Let recursion go all the way to index 0 to catch hidden zeros
            if target == 0 and array[index] == 0:           # 2 - choices: Include the 0 or exclude the 0
                return 2
            elif target == 0 or array[index] == target:     # 1 - choice: Either target is met, or this element finishes it
                return 1
            return 0
        if dp[index][target] != -1:
            return dp[index][target]
        not_take = self.func(index - 1, target, array, dp)
        take = 0
        if array[index] <= target:
            take = self.func(index - 1, target - array[index], array, dp)
        dp[index][target] = take + not_take
        return dp[index][target]
    
    def perfectSum(self, arr, target):
        dp = [[-1 for _ in range(target + 1)]for _ in range(len(arr))]
        return self.func(len(arr) - 1, target, arr, dp)      

# sol = Solution()
# print(sol.perfectSum([5, 2, 3, 10, 6, 8], 10))

                        # -- Dynamic Programming Tabulation Soln. -- 

def countSubsets(nums, target):
    n = len(nums)
    dp = [[0 for _ in range(target + 1)] for _ in range(n)]

    # Base case for the first element ONLY
    dp[0][0] = 1                # 1 way to pick empty set for sum 0

    if nums[0] == 0:
        dp[0][0] = 2            # Including or excluding nums[0] both yield sum 0
    elif nums[0] <= target:
        dp[0][nums[0]] = 1      # 1 way to form sum equal to nums[0]

    for i in range(1, n):
        for s in range(target + 1):
            not_take = dp[i-1][s]
            take = 0
            if nums[i] <= s:
                take = dp[i-1][s - nums[i]]
            dp[i][s] = not_take + take
            
    return dp[n-1][target]

# --------------------------------------------------------------------------------------------------
# PROBLEM - Partitions with Given Difference - Given an array arr[] and an integer diff, count the number of ways to partition the array 
#           into two subsets such that the difference between their sums is equal to diff.
#           A partition means dividing an array into two subsets say S1 and S2 such that the union of S1 and S2 is equal to the original array and each element is present in only one of the subsets.
class Solution:                             # -- Dynamic Programming Memoization Soln. -- 
    MOD = 10**9 + 7                         # • Time Col: (N x target); Space Col: (N x target);
    def func(self, index, target, array, dp):
        if index == 0:
            if target == 0 and array[0] == 0:
                return 2  # Pick array[0] or don't pick array[0]
            if target == 0 or array[0] == target:
                return 1  # Pick array[0] (if equal) or don't pick (if target == 0)
            return 0

        if dp[index][target] != -1:
            return dp[index][target]

        not_take = self.func(index - 1, target, array, dp)
        take = 0
        if array[index] <= target:
            take = self.func(index - 1, target - array[index], array, dp)
        dp[index][target] = (take + not_take) % self.MOD
        return dp[index][target]

    def perfectSum(self, arr, target):
        n = len(arr)
        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]
        return self.func(n - 1, target, arr, dp)

    def countPartitions(self, arr, diff):
        total_sum = sum(arr)
        if total_sum < diff or (total_sum - diff) % 2 != 0:
            return 0
        target = (total_sum - diff) // 2
        return self.perfectSum(arr, target)
    

class Solution:                         # -- Dynamic Programming Memoization Soln. -- 
    MOD = 10**9 + 7                     # • Time Col: (N x target); Space Col: (N x target);
    def countSubsets(self, nums, target):
        n = len(nums)
        dp = [[0 for _ in range(target + 1)] for _ in range(n)]

        # Base case for the first element ONLY
        dp[0][0] = 1                # 1 way to pick empty set for sum 0
        if nums[0] == 0:
            dp[0][0] = 2            # Including or excluding nums[0] both yield sum 0
        else:
            dp[0][0] = 1

        if nums[0] != 0 and nums[0] <= target:
            dp[0][nums[0]] = 1      # 1 way to form sum equal to nums[0]

        for i in range(1, n):
            for s in range(target + 1):
                not_take = dp[i-1][s]
                take = 0
                if nums[i] <= s:
                    take = dp[i-1][s - nums[i]]
                dp[i][s] = (not_take + take) % self.MOD

        return dp[n-1][target]
     
    def countPartitions(self, arr, diff):
        total_sum = sum(arr)
        if total_sum < diff or (total_sum - diff) % 2 != 0:
            return 0
        target = (total_sum - diff) // 2
        return self.countSubsets(arr, target)

# --------------------------------------------------------------------------------------------------
# 3882. Minimum XOR Path in a Grid - Given a m x n grid filled with non-negative integers, find a path from top-left (0,0) to
#       bottom-right (m-1, n-1), moving only right or down, which minimizes the bitwise XOR of all values 
                               # along the path (including both endpoints).
class Solution:
    def f(self, i, j, grid, dp):
        if i == 0 and j == 0:           # Time - O(n·m·K) where K = max set size;  Space - O(n·m·K)
            return {grid[0][0]}
        if i < 0 or j < 0:
            return set()                # Note: Unlike min-path-sum, XOR is not monotonic, so DP must track the
        if dp[i][j] != -1:              # set of all reachable XORs per cell — not a single best value.
            return dp[i][j]

        # Get all reachable XOR paths from UP and LEFT
        up_paths = self.f(i - 1, j, grid, dp)
        left_paths = self.f(i, j - 1, grid, dp)

        # Compute new XOR totals for current cell
        res = set()
        for p in up_paths:
            res.add(p ^ grid[i][j])
        for p in left_paths:
            res.add(p ^ grid[i][j])

        dp[i][j] = res
        return dp[i][j]

    def minCost(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        
        all_possible_xors = self.f(n - 1, m - 1, grid, dp)
        return min(all_possible_xors)

# --------------------------------------------------------------------------------------------------











































































































































































































































