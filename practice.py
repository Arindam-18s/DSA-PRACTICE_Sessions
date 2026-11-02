# 462. Minimum Moves to Equal Array Elements II - Given an integer array nums of size n, 
# return the minimum number of moves required to make all array elements equal.
                        # In one move, you can increment or decrement an element of the array by 1.
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        minimum = min(nums)
        mid = len(nums) // 2
        maps = {}

        for i in range(len(nums)):
            diff = abs(nums[mid] - nums[i])
            maps[i] = diff

        res = 0
        for val in maps.values():
            res += val
        return res


sol = Solution()
print(sol.minMoves2([1, 2, 3]))