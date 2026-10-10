def fibo_using_dp(n, dp):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    return fibo_using_dp(n - 1, dp) + fibo_using_dp(n - 2, dp)

if __name__ == "__main__":
    n = 6
    dp = [-1] * (n + 1)
    print(fibo_using_dp(n, dp))