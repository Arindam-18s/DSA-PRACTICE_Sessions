class Solution:
    def climbStairs_Tabulation(self, n: int, costs: List[int]) -> int:     # Time -> O(N), Space -> O(N)
        dp = [-1] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            cost = float('inf')
            j = i + 1
            if j <= n:                                  # Jump of 1 Step
                cost = (costs[j - 1] + (j - i) * (j - i)) + dp[j]
            j = i + 2
            if j <= n:                                  # Jump of 2 Step
                cost = min(cost, (costs[j - 1] + (j - i) * (j - i)) + dp[j])
            j = i + 3
            if j <= n:                                  # Jump of 3 Step
                cost = min(cost, (costs[j - 1] + (j - i) * (j - i)) + dp[j])

            dp[i] = cost
        return dp[0] 


    def rec_CS_II(self, i, n, dp, costs):                                  # Time -> O(N), Space -> O(N)
        if i == n:                      #   _____________________________
            return 0                    #   |   |   |   |   |   |   |   |
        if dp[i] != -1:                 #   ````````````````````````````
            return dp[i]                              #  <---------------               
        cost = float('-inf')            # Traversing from back to the front Top Down DP
        j = i + 1
        if j <= n:                                  # Jump of 1 Step
            cost = (costs[j - 1] + ((j - i) ** 2)) + self.rec_CS_II(j, n, dp, costs)
        j = i + 2
        if j <= n:                                  # Jump of 2 Step
            cost = min(cost, (costs[j - 1] + ((j - i) ** 2)) + self.rec_CS_II(j, n, dp, costs))
        j = i + 3
        if j <= n:                                  # Jump of 3 Step
            cost = min(cost, (costs[j - 1] + ((j - i) ** 2)) + self.rec_CS_II(j, n, dp, costs))

        dp[i] = cost
        return dp[i]

    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [-1] * n
        return self.rec_CS_II(0, n, dp, costs)
