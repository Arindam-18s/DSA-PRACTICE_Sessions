def subset_sum_eq_K_Tabulation(array, k):
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
