import sys
sys.setrecursionlimit(10**9)
class Solution:
    # 1. Pure Recursive Approach
    def rec(self, index: int, theifs_bag: int, items_val: list[int], items_weight: list[int]) -> int:
        if index == 0:                              # Guranted TLE
            if items_weight[0] <= theifs_bag:
                return items_val[0]
            return 0

        not_take = 0 + self.rec(index - 1, theifs_bag, items_val, items_weight)
        take = float('-inf')
        if theifs_bag >= items_weight[index]:
            take = items_val[index] + self.rec(index - 1, theifs_bag - items_weight[index], items_val, items_weight)

        return max(take, not_take)

    # 2. Memoization (Top-Down DP)
    def rec_memoization_helper(self, index: int, theifs_bag: int, items_val: list[int], items_weight: list[int], dp: list[list[int]]) -> int:
        if index == 0:
            if items_weight[0] <= theifs_bag:
                return items_val[0]
            return 0

        if dp[index][theifs_bag] != -1:
            return dp[index][theifs_bag]

        not_take = 0 + self.rec_memoization_helper(index - 1, theifs_bag, items_val, items_weight, dp)
        take = float('-inf')
        if theifs_bag >= items_weight[index]:
            take = items_val[index] + self.rec_memoization_helper(index - 1, theifs_bag - items_weight[index], items_val, items_weight, dp)

        dp[index][theifs_bag] = max(take, not_take)
        return dp[index][theifs_bag]

    def knapsack_memoization(self, theifs_bag: int, items_val: list[int], items_weight: list[int]) -> int:
        n = len(items_val)
        dp = [[-1 for _ in range(theifs_bag + 1)] for _ in range(n)]
        return self.rec_memoization_helper(n - 1, theifs_bag, items_val, items_weight, dp)

    # 3. Tabulation (Bottom-Up DP)
    def knapsack_Tabulation(self, theifs_bag: int, items_val: list[int], items_weight: list[int]) -> int:
        n = len(items_val)
        dp = [[0 for _ in range(theifs_bag + 1)] for _ in range(n)]

        # Base case: populating for item 0 across valid capacity weights
        for w in range(items_weight[0], theifs_bag + 1):
            dp[0][w] = items_val[0]

        # Fill table bottom-up
        for index in range(1, n):
            for w in range(theifs_bag + 1):
                not_take = dp[index - 1][w]
                take = float('-inf')
                if items_weight[index] <= w:
                    take = items_val[index] + dp[index - 1][w - items_weight[index]]

                dp[index][w] = max(not_take, take)

        return dp[n - 1][theifs_bag]

sol=Solution()
print(sol.knapsack_memoization(6, [30, 40, 60], [3, 2, 5]))
print(sol.knapsack_Tabulation(6, [30, 40, 60], [3, 2, 5]))