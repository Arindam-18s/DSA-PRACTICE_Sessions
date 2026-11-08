
# 4107. Count Valid Suffix Sorts I - given two integer arrays nums and target, both of length n.
                # For each index i, consider sorting the suffix nums[i..n - 1] of the original array in non-increasing order
class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> int:
        nums = [7,6,8]
        target = [8, 6, 7]                 # Input: nums = [1,5,6,4,6], target = [1,5,6,6,4]
        res = []                           # Output: 2

        n = len(nums)
        prefix = []
        suffix = []
        for i in range(n):
            prefix = nums[0:i]
            suffix = nums[i:n]
            suffix_2 = sorted(suffix, reverse=True)
            res.append(prefix + suffix_2)

            # res.append(nums[0:i] + nums[i : n + 1])
        print(res)

        count = 0
        for arr in res:
            if arr == target:
                count += 1

        print(count)





