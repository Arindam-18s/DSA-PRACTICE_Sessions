# # PROBLEM - Count Subsets with Sum K | Given an array arr[] of non-negative integers and an integer target, 
# # count all subsets of the array whose sum is equal to the given target. Input: arr[] = [5, 2, 3, 10, 6, 8], target = 10
#                             # Explanation: The subsets {5, 2, 3}, {2, 8}, and {10} sum up to the target 10.   Output: 3
#                             # -- Dynamic Programming Memoization Soln. -- 
# class Solution:                             # • Time Col: (N x target); Space Col: (N x target);
#     def func(self, index, target, array, dp):       
#         if index == 0:                                      # Let recursion go all the way to index 0 to catch hidden zeros
#             if target == 0 and array[index] == 0:           # 2 - choices: Include the 0 or exclude the 0
#                 return 2
#             elif target == 0 or array[index] == target:     # 1 - choice: Either target is met, or this element finishes it
#                 return 1
#             return 0
#         if dp[index][target] != -1:
#             return dp[index][target]
#         not_take = self.func(index - 1, target, array, dp)
#         take = 0
#         if array[index] <= target:
#             take = self.func(index - 1, target - array[index], array, dp)
#         dp[index][target] = take + not_take
#         return dp[index][target]
    
#     def perfectSum(self, arr, target):
#         dp = [[-1 for _ in range(target + 1)]for _ in range(len(arr))]
#         return self.func(len(arr) - 1, target, arr, dp)      

# sol = Solution()
# print(sol.perfectSum([5, 2, 3, 10, 6, 8], 10))



a = 5
b = 15

s1 = f"{a:016b}"
s2 = f"{b:016b}"

inner_s1, inner_s2 = int(s1), int(s2)
a_count = 0
b_count = 0

while inner_s1 > 0 or inner_s2 > 0:
    digit1 = inner_s1 % 10
    digit2 = inner_s2 % 10
    if digit1 == 1:
        a_count += 1
    if digit2 == 1:
        b_count += 1
    inner_s1 = inner_s1 // 10
    inner_s2 = inner_s2 // 10

print(a_count, b_count)
if a_count >= b_count:
    print(a_count * b_count) 
else:
    print(b_count // a_count)
