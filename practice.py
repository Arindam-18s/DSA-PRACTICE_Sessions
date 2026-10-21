def subset_sum_equals_k(index, target, array):
    if target == 0:
        return True
    if index < 0:
        return False
    if index == 0:
        if array[index] == target:
            return True
    if dp[index][target] != -1:
        return dp[target]
    not_take = subset_sum_equals_k(index - 1, target, array)
    take = False
    if target >= array[index]:
        not_take = subset_sum_equals_k(index - 1, target - array[index], array)

    dp[index][target] = take or not_take
    return dp[index][target]

if __name__ == "__main__":
    array = [1, 3, 2, 4]
    k = 11
    # Initialize a 2D list with -1 of size (n) x (k + 1)
    # Rows represent the index (0 to n-1), Columns represent the target (0 to k)
    dp = [[-1 for _ in range(k + 1)] for _ in range(len(array))]
    print(subset_sum_equals_k(len(array) - 1, k, array))



if __name__ == "__main__":
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
            


    
