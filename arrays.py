# Multiple Occurance of a element

# Bad solution - with bad time complexity
arr1 = [1, 3, 2, 1] 
temp = [] 

for i in range(len(arr1)): 
    if arr1[i] not in temp: 
        temp.append(arr1[i]) # Correctly adds the item to the tracking list
    else: 
        pass
        # print("element", arr1[i], "occurred multiple times") 

# improved solution - with good time complexity
arr2 = [1, 4, 2, 2]
seen = set()        #HashSets cannot have duplicate values

for item in arr2:
    if item in seen:
        pass
        # print(f"element {item} occurred multiple times")
    else:
        seen.add(item)

#------------------------------------------------------------------------------- 
#  896. Monotonic Array - O(n) soln
class Solution(object):
    def isMonotonic(self, nums):
        for i in range(len(nums)):
            lastele = i

        if nums[0] < nums[lastele]:
            for i in range(len(nums) - 1):
                if nums[i] <= nums[i+1]:
                    continue
                else:
                    return False
            return True
        else:
            for i in range(len(nums) - 1):
                if nums[i] >= nums[i+1]:
                    continue
                else:
                    return False
            return True

# ------------------------------------------------- 
# 189. Rotate Array  -> Input: nums = [1,2,3,4,5,6,7], k = 3, Output: [5,6,7,1,2,3,4]

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        temp = [0] * n
        for i in range(n):
            new_index = (i + k) % n
            temp[new_index] = nums[i]
            return temp
        
# ------------------------------------------------- 
# Leetcode - 242. Valid Anagram   
class Solution(object):         # Time col- O(n^2)
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        temp = list(s)
        for char in t:
            if char in temp:
                temp.remove(char)
            else:
                return False
        return True
    
class Solution(object):             # Time col- O(n)
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
            
        counts = [0] * 26
        
        # Single loop to populate the frequency array
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
            
        return not any(counts)          # Check if any count is not zero using Python's built-in any()

# ------------------------------------------------- 
# 561. Array Partition    
class Solution(object):
    def arrayPairSum(self, nums):
        sum = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            sum = sum + nums[i]
        return sum
    
# ------------------------------------------------- 
# 1291. Sequential Digits
result = []
sample = "123456789"
low = high = "Something"
        
# Loop through all possible lengths of sequential numbers (from 2 digits to 9 digits)
for length in range(2, 10):
            # Slide a window across the sample string
            for start in range(10 - length):
                substring = sample[start : start + length]
                num = int(substring)
                
                # Check if the generated number fits in your range
                if low <= num <= high:
                    result.append(num)
                elif num > high:
                    break # Stop early if numbers get too large
                    
print(result)
# ------------------------------------------------- 
# two sum - II
class Solution(object):
    def twoSum(self, numbers, target):
        n = len(numbers)
        left = 0
        right = n-1
        while(left < right):
            sum = numbers[left] + numbers[right]
            if(sum == target):
                return [left + 1, right + 1]
            elif(sum > target):
                right = right - 1
            else:
                left = left + 1
        return [-1,-1]    
# ------------------------------------------------- 
# 15  -   3-SUM
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        result = set()
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            
            while j < k:
                target = nums[i] + nums[j] + nums[k]
                if target == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif target > 0:
                    k -= 1
                else:
                    j += 1
                    
        return [list(triplet) for triplet in result]
# ------------------------------------------------- 
# 26. Remove Duplicates from Sorted Array  
class Solution(object):
    def removeDuplicates(self, nums):
        l = 1
                                           #_________________________________________
        for r in range(1, len(nums)):      #|_0_|_0_|_1_|_1_|_1_|_2_|_3_|_3_|_4_|_4_|
            if nums[r] != nums[r - 1]:     #      L -> only moves when we had found a unique element
                nums[l] =  nums[r]         #      R -> moves with the for loop
                l = l + 1
        return l
# ------------------------------------------------- 
# 2D - Arrays

rows, cols = 4, 4
s = "PAYPALISHIRING"
numRows = 4

grid = []
for i in range(cols):
    col = []
    for j in range(rows):
        col.append("")
    grid.append(col)

char_index = 0
for i in range(cols):       # Fill the grid column-wise
    for j in range(rows):   
        if char_index < len(s):
            grid[j][i] = s[char_index]
            char_index += 1

for row in grid:            # Print the grid row-by-row to see the result
    print(row)

# -------------------------------------------------------------------------------
