class Solution:
    MOD = 10**9 + 7
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
    

class Solution:
    MOD = 10**9 + 7
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

