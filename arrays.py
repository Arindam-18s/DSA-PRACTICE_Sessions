# 896. Monotonic Array - O(n) soln

class Solution(object):
    def isMonotonic(self, nums):
        for i in range(len(nums)):
            lastele = i

        if nums[0] < nums[lastele]:
            for i in range(len(nums) - 1):
                if nums[i] <= nums[i + 1]:
                    continue
                else:
                    return False
            return True
        else:
            for i in range(len(nums) - 1):
                if nums[i] >= nums[i + 1]:
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

class Solution(object):  # Time col- O(n^2)
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

class Solution(object):  # Time col- O(n)
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        counts = [0] * 26
        for i in range(len(s)):     # Single loop to populate the frequency array
            counts[ord(s[i]) - ord("a")] += 1
            counts[ord(t[i]) - ord("a")] -= 1

        return not any(
            counts
        )  # Check if any count is not zero using Python's built-in any()

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

def Sequencial_Digit():
    result = []
    sample = "123456789"
    low = high = "Something"
    for length in range(2, 10):  # Loop through all possible lengths of sequential numbers (from 2 digits to 9 digits)
        # Slide a window across the sample string
        for start in range(10 - length):
            substring = sample[start : start + length]
            num = int(substring)

            if low <= num <= high:  # Check if the generated number fits in your range
                result.append(num)
            elif num > high:
                break  # Stop early if numbers get too large
    print(result)

# -------------------------------------------------
# two sum - II

class Solution(object):
    def twoSum(self, numbers, target):
        n = len(numbers)
        left = 0
        right = n - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right = right - 1
            else:
                left = left + 1
        return [-1, -1]

# -------------------------------------------------
# 15 - 3-SUM

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
        l = 1                          # _________________________________________
        for r in range(1, len(nums)):  # |_0_|_0_|_1_|_1_|_1_|_2_|_3_|_3_|_4_|_4_|
            if (
                nums[r] != nums[r - 1]
            ):  #      L -> only moves when we had found a unique element
                nums[l] = nums[r]  #      R -> moves with the for loop
                l = l + 1
        return l

# -------------------------------------------------
# 2D - Arrays

def TwoD_Arrays():
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
    for i in range(cols):  # Fill the grid column-wise
        for j in range(rows):
            if char_index < len(s):
                grid[j][i] = s[char_index]
                char_index += 1

    for row in grid:  # Print the grid row-by-row to see the result
        print(row)

# -------------------------------------------------------------------------------
# Fibonacci - calculate the closest Fibonacci index and generates the surrounding sequence.

import math
def get_fibonacci_neighbors(X, count=3):
    # Finds the closest Fibonacci number to X and scales up/down by 'count' steps using the Golden Ratio.
    if X <= 0:
        return "Please enter a positive number greater than 0."

    PHI = (1 + math.sqrt(5)) / 2  # The Golden Ratio (~1.6180339887)

    # Step 1: Estimate the index 'n' using the logarithmic formula
    n = round(math.log(X * math.sqrt(5), PHI))

    # Step 2: Calculate the exact baseline Fibonacci number using Binet's formula
    closest_fib = round((PHI**n) / math.sqrt(5))

    # Step 3: Scale up using multiplication
    bigger = []
    current = closest_fib
    for _ in range(count):
        current = round(current * PHI)
        bigger.append(current)

    # Step 4: Scale down using division
    smaller = []
    current = closest_fib
    for _ in range(count):
        current = round(current / PHI)
        smaller.append(current)

    smaller.reverse()  # Reverse smaller list to keep chronological order

    return {"Target Input": X, "Closest Fibonacci": closest_fib, f"Next {count} Smaller": smaller, f"Next {count} Bigger": bigger, }

# --- Example Usage ---
if __name__ == "__main__":
    random_number = 1000
    result = get_fibonacci_neighbors(random_number, count=3)

    # print(f"Results for input: {result['Target Input']}")
    # print(f"Closest Fibonacci: {result['Closest Fibonacci']}")
    # print(f"Smaller Neighbors: {result[f'Next 3 Smaller']}")
    # print(f"Bigger Neighbors:  {result[f'Next 3 Bigger']}")

# -------------------------------------------------------------------------------
# Basic Array Operations 

class Basic_Array_Prblems():
    def largest_el_in_array(self, arr):      # Tcol -> 0(N Log N)
        arr.sort()      # Brute force method is to sort the Array and reyturn the last el
        return arr[len(arr) - 1]

    def largest_el_in_array_optimal(self, arr):
        largest = arr[0]                     # Tcol -> 0(Log N)
        for i in range(len(arr)):   # Optimal Soln is to set the first el as largest and update it as we go(iterate), 
            if arr[i] >= largest:   # if any element larger than the current largest occurs
                largest = arr[i]
        return largest

    def second_largest_el_in_array(self, arr):
        largest = arr[0]                     # Tcol -> 0(Log N)
        second_largest = float('-inf')
        for i in range(len(arr)):
            if arr[i] > largest:
                second_largest = largest
                largest = arr[i]
        return largest, second_largest       # returns Tupple

    def second_smallest_el_in_array(self, arr):
        smallest = arr[0]                    # Tcol -> 0(Log N)
        second_smallest = float('inf')
        for i in range(len(arr)):
            if arr[i] < smallest:
                second_smallest = smallest
                smallest = arr[i]
            elif arr[i] < second_smallest:
                second_smallest = arr[issubclass]
        return smallest, second_smallest     # returns Tupple

    def check_if_array_is_Sorted(self, arr):
        for i in range(len(arr)):            # Tcol -> 0(Log N)
            if arr[i] > arr[i - 1]:
                continue
            else:
                return False
        return True                          # Return True/False

    def remove_duplicates_from_sorted_array(self, arr):   # Have To Do it In-Place Without any extra space
        # [1, 1, 2, 2, 2, 3, 4, 5, 5, 5] -> [1, 2, 3, 4, 5, _, _, _, _, _]

        # We will be using the Two-Pointer Optimal Approach --- Tcol - O(N), Scol - O(1)
        i = 0 
        for j in range(len(arr)):
            if arr[j] != arr[i]:        # j will move forwars and check if any unique elemnt is in the array rathar tham
                arr[i + 1] = arr[j]     # the current i, when it finds that, we put that el in front of i'th position 
                i += 1                  # And we move i along, util j is in bound, at last we shall have 
                                        # all the unique elements plotted until the i+1'th position in the array In-Place
        return arr[ : (i + 1)]

    
if __name__ == "__main__":
    array = [5, 7, 1, 2, 9, 3, 8]
    array2 = [1, 1, 2, 2, 2, 3, 3, 4]
    sol = Basic_Array_Prblems()
    # print(sol.largest_el_in_array(array))
    # print(sol.largest_el_in_array_optimal(array))
    # print(sol.second_largest_el_in_array(array))
    # print(sol.second_smallest_el_in_array(array))
    # print(sol.remove_duplicates_from_sorted_array(array2))

# -------------------------------------------------------------------------------
# Given an array arr[], Left rotate an array by 1 place

def left_rotate_Array_by_1_Place(array):   # Tcol - O(N), Scol - Space used - (O(N)) cause we are using the existing array
    temp = array[0]                                             #Extra Space - O(1)
    i, j = 0, 1
    while(j < len(array)):
        array[i] = array[j]                # array = [1, 2, 3, 4, 5, 6], O/p = [2, 3, 4, 5, 6, 1]
        i += 1
        j += 1
    array[len(array) - 1] = temp
    return array

# -------------------------------------------------------------------------------
# Given an array arr[], Left rotate an array by `D`  places 

                                          # Tcol - O(len(array) + D), Scol - Extra Space -> O(D)
def left_rotate_Array_by_D_Places(D, array):
    if D > len(array):          # If D is larger than length of the array, then we only rotate to places until
        D = D % len(array)      # the mod of D % n = Extra plcs., cause Rotating N places is just getting the same Arr back

    temp = []
    for j in range(D):          # Storing the places that we are actually gonna append at the last of the array
        temp.append(array[j])              
                                            # array = [1, 2, 3, 4, 5, 6] , D = 8    |    O/P = [3, 4, 5, 6, 1, 2]
    i, j = 0, D
    while(j < len(array)):      # Rotating the array until Len(array) - D places
        array[i] = array[j]
        i += 1
        j += 1

    inserting_index = len(array) - D    
    k = 0
    while(inserting_index < len(array)):    # Putting the the remaining D elements to the back of the main array
        array[inserting_index] = temp[k]    # To complete the rotation
        inserting_index += 1
        k += 1
    return array

def left_rotate_Array_by_D_Places_Optimal_Soln(D, array):
    if D > len(array):          # If D is larger than length of the array, then we only rotate to places until
        D = D % len(array)      # the mod of D % n = Extra plcs., cause Rotating N places is just getting the same Arr back

    array = reverse(0, D)
    array = reverse(D, len(array))
    array = reverse(0, len(array))
    def reverse(start, end):
        while start <= end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1
    return array

# -------------------------------------------------------------------------------

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6]
    print(left_rotate_Array_by_D_Places(8, array))
    print(left_rotate_Array_by_D_Places_Optimal_Soln(8, array))