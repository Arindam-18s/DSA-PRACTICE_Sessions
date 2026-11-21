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
        for i in range(len(s)):  # Single loop to populate the frequency array
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
    for length in range(
        2, 10
    ):  # Loop through all possible lengths of sequential numbers (from 2 digits to 9 digits)
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
        l = 1  # _________________________________________
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

    return {
        "Target Input": X,
        "Closest Fibonacci": closest_fib,
        f"Next {count} Smaller": smaller,
        f"Next {count} Bigger": bigger,
    }

# --- Example Usage ---
if __name__ == "__main__":
    random_number = 1000
    result = get_fibonacci_neighbors(random_number, count=3)

    # print(f"Results for input: {result['Target Input']}")
    # print(f"Closest Fibonacci: {result['Closest Fibonacci']}")
    # print(f"Smaller Neighbors: {result[f'Next 3 Smaller']}")
    # print(f"Bigger Neighbors:  {result[f'Next 3 Bigger']}")

# -----------------------------------------------------------------------------------------------------------
# Basic Array Operations

class Basic_Array_Prblems:
    def largest_el_in_array(self, arr):  # Tcol -> 0(N Log N)
        arr.sort()  # Brute force method is to sort the Array and reyturn the last el
        return arr[len(arr) - 1]

    def largest_el_in_array_optimal(self, arr):
        largest = arr[0]  # Tcol -> 0(Log N)
        for i in range(len(arr)):  # Optimal Soln is to set the first el as largest and update it as we go(iterate),
            if (arr[i] >= largest):  # if any element larger than the current largest occurs
                largest = arr[i]
        return largest

    def second_largest_el_in_array(self, arr):
        largest = arr[0]  # Tcol -> 0(Log N)
        second_largest = float("-inf")
        for i in range(len(arr)):
            if arr[i] > largest:
                second_largest = largest
                largest = arr[i]
        return largest, second_largest  # returns Tupple

    def second_smallest_el_in_array(self, arr):
        smallest = arr[0]  # Tcol -> 0(Log N)
        second_smallest = float("inf")
        for i in range(len(arr)):
            if arr[i] < smallest:
                second_smallest = smallest
                smallest = arr[i]
            elif arr[i] < second_smallest:
                second_smallest = arr[issubclass]
        return smallest, second_smallest  # returns Tupple

    def check_if_array_is_Sorted(self, arr):
        for i in range(len(arr)):  # Tcol -> 0(Log N)
            if arr[i] > arr[i - 1]:
                continue
            else:
                return False
        return True  # Return True/False

    def remove_duplicates_from_sorted_array(self, arr):  # Have To Do it In-Place Without any extra space
                                                        # [1, 1, 2, 2, 2, 3, 4, 5, 5, 5] -> [1, 2, 3, 4, 5, _, _, _, _, _]
        # We will be using the Two-Pointer Optimal Approach --- Tcol - O(N), Scol - O(1)

        i = 0
        for j in range(len(arr)):
            if (arr[j] != arr[i]):   # j will move forwars and check if any unique elemnt is in the array rathar tham
                arr[i + 1] = arr[j]  # the current i, when it finds that, we put that el in front of i'th position
                i += 1               # And we move i along, util j is in bound, at last we shall have
        return arr[: (i + 1)]        # all the unique elements plotted until the i+1'th position in the array In-Place

if __name__ == "__main__":
    array = [5, 7, 1, 2, 9, 3, 8]
    array2 = [1, 1, 2, 2, 2, 3, 3, 4]
    sol = Basic_Array_Prblems()
    # print(sol.largest_el_in_array(array))
    # print(sol.largest_el_in_array_optimal(array))
    # print(sol.second_largest_el_in_array(array))
    # print(sol.second_smallest_el_in_array(array))
    # print(sol.remove_duplicates_from_sorted_array(array2))

# -----------------------------------------------------------------------------------------------------------
# Given an array arr[], Left rotate an array by 1 place

def left_rotate_Array_by_1_Place(array,):  # Tcol - O(N), Scol - Space used - (O(N)) cause we are using the existing array
    temp = array[0]  # Extra Space - O(1)
    i, j = 0, 1
    while j < len(array):
        array[i] = array[j]  # array = [1, 2, 3, 4, 5, 6], O/p = [2, 3, 4, 5, 6, 1]
        i += 1
        j += 1
    array[len(array) - 1] = temp
    return array

# -----------------------------------------------------------------------------------------------------------
# Given an array arr[], Left rotate an array by `D`  places

                        # Tcol - O(len(array) + D), Scol - Extra Space -> O(D)
def left_rotate_Array_by_D_Places(D, array):
    if D > len(array):  # If D is larger than length of the array, then we only rotate to places until
        D = D % len(array)  # the mod of D % n = Extra plcs., cause Rotating N places is just getting the same Arr back

    temp = []
    for j in range(D):  # Storing the places that we are actually gonna append at the last of the array
        temp.append(array[j])
        # array = [1, 2, 3, 4, 5, 6] , D = 8    |    O/P = [3, 4, 5, 6, 1, 2]
    i, j = 0, D
    while j < len(array):  # Rotating the array until Len(array) - D places
        array[i] = array[j]
        i += 1
        j += 1

    inserting_index = len(array) - D
    k = 0
    while inserting_index < len(array):  # Putting the the remaining D elements to the back of the main array
        array[inserting_index] = temp[k]  # To complete the rotation
        inserting_index += 1
        k += 1
    return array

    # Tcol - O(2n), Scol - Extra Space -> O(1)   |   Optimal Solution
def left_rotate_Array_by_D_Places_Optimal_Soln(D, array):
    if D > len(array):  # If D is larger than length of the array, then we only rotate to places until
        D = D % len(array)  # the mod of D % n = Extra plcs., cause Rotating N places is just getting the same Arr back

    def reverse(start, end):
        while start <= end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1

    N = len(array)
    reverse(0, D - 1)  # Reverse first D elements
    reverse(D, N - 1)  # Reverse remaining elements
    reverse(0, N - 1)  # Reverse the entire array
    return array

# -----------------------------------------------------------------------------------------------------------
# 189. Rotate Array - Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
                    # nums = [1,2,3,4,5,6,7], k = 3     |     Output: [5,6,7,1,2,3,4]

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        N = len(nums)
        if k > N:
            k = k % N

        def reverse(start, end):
            while start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(N - k, N - 1)  # Reverse The Last K elements
        reverse(0, N - k - 1)  # Reverse remaining elements from the first
        reverse(0, N - 1)  # Reverse the entire array
        return nums


# -----------------------------------------------------------------------------------------------------------
# 283. Move Zeroes - Given an integer array nums, move all 0's to the end of it while maintaining
                   # the relative order of the non-zero elements. - IN PLACE

class Solution:
    def moveZeroes_brute_Force(self, nums: list[int]):  # Brute Force - Tcol - O(2N) , Scol - extraSpace - O(N)
        temp = []
        no_of_zeroes = 0
        for i in range(len(nums)):
            if (nums[i] != 0):  #   [0,1,0,3,12,-23,-4,0,1,0] ->  [1, 3, 12, -23, -4, 1, 0, 0, 0, 0]
                temp.append(nums[i])
            else:
                no_of_zeroes += 1

        while no_of_zeroes > 0:
            temp.append(0)
            no_of_zeroes -= 1

        for i in range(len(nums)):
            nums[i] = temp[i]
        return nums

    def moveZeroes_Optimal_using_TwoPointers(self, nums: list[int]):  # Tcol - O(N), Scol - O(1)/extraSpace - None
        zero_starts_at = -1

        for i in range(len(nums)):  #   [0,1,0,3,12,-23,-4,0,1,0] ->  [1, 3, 12, -23, -4, 1, 0, 0, 0, 0]
            if nums[i] == 0:
                zero_starts_at = i
                break

        if (zero_starts_at == -1):  # If there is no zeroes in the array, we do no calculations
            return nums

        j = zero_starts_at  #  J will be always at a Zero
        i = j + 1  #  And i Will be simply Iterating
        while i < len(nums):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
                i += 1
            else:
                i += 1
        return nums

# -----------------------------------------------------------------------------------------------------------
# Problem - Union of Two Sorted Arrays - Return Union of two sorted arrays combines all unique elements
# from both arrays into a single sorted array, But Don't Repeat any elements.
# Input: a[] = [1, 2, 3, 4, 5],     b[] = [1, 2, 3, 6, 7]  |    Output: [1 2 3 4 5 6 7]

class Solution:
    def findUnion_brute_Force(self, arr1, arr2):  # Time Complexity: O ((N + M)log(N + M))
        union_set = set()  # Space Complexity: O(N + M) extra space used by union_set
        for i in range(len(arr1)):
            union_set.add(arr1[i])

        for j in range(len(arr2)):
            union_set.add(arr2[j])

        op = list(union_set)
        return sorted(op)

                                # Optimal Soln. This runs in O(N1 + N2) time
    def findUnion_Optimal_Soln(self, arr1: list, arr2: list):  # and O(N1 + N2) auxiliary space (for the output list)
        N1, N2 = len(arr1), len(arr2)  # Where N1 = Length of arr1, and N2 = Length of arr2
        i = j = 0                      # Two pointers to traverse arr1 and arr2
        union_array = []               # Stores the final sorted union without duplicates
                                       # Traverse both arrays simultaneously until one reaches the end
        while i < N1 and j < N2:
            if arr1[i] <= arr2[j]:      # Append only if union_array is empty or the last element is different
                if (len(union_array) < 1) or union_array[len(union_array) - 1] != arr1[i]:
                    union_array.append(arr1[i])
                i += 1
            else:                       # Append arr2[j] if it's not a duplicate of the last added element
                if (len(union_array) < 1) or union_array[len(union_array) - 1] != arr2[j]:
                    union_array.append(arr2[j])
                j += 1                  # Append any remaining unique elements from arr2
        
        while j < N2:
            if (len(union_array) < 1) or union_array[len(union_array) - 1] != arr2[j]:
                union_array.append(arr2[j])
                j += 1                  # Append any remaining unique elements from arr1

        while i < N1:
            if (len(union_array) < 1) or union_array[len(union_array) - 1] != arr1[i]:
                union_array.append(arr1[i])
                i += 1

        return union_array

# -----------------------------------------------------------------------------------------------------------
# 349. Intersection of Two Arrays - Given two integer arrays nums1 and nums2, return an array of their intersection.
            # Each element in the result must be unique and you may return the result in any order.
            # `Repeatation` of SAME array elements allowed if multiple corresponding same elements exists in both arrays

class Solution:  # Brute Force Appr.
    def intersection_Brute_Force(self, nums1: list[int], nums2: list[int]) -> list[int]:
        N1, N2 = len(nums1), len(nums2)  # TimeCol: O(N1 x N2), SpaceCol: O(N2)
        Used = [-1] * N2  # N1 = len(nums1), N2 = len(nums2)
        intersection_array = []
        for i in range(N1):  # Iterate through each element in nums1
            for j in range(N2):  # Search for a matching element across nums2
                if (nums1[i] == nums2[j]) and (Used[j] == -1):  # Check if values match and nums2[j] hasn't been paired yet
                    # if nums1[i] not in intersection_array:    # If we Only wanna allow an Item only Once in the O/P Arr
                    intersection_array.append(nums1[i])
                    Used[j] = 1
                    break
            # if nums2[j] > nums1[i]:     # If the Array is Guranteed to be Sorted
            #     break
        return intersection_array

                                        # Optimal Soln. for intersection /w TWO POINTER APPROACH
    def intersection_Optimal_Soln(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()                    # Tcol - O(N1 + N2), Scol - No extra Space - O(1)
        N1, N2 = len(nums1), len(nums2)
        i = j = 0
        intersection_array = []
        while i < N1 and j < N2:
            if (nums1[i] < nums2[j]):  # Whenever The elements Dont Match move the index which has the lowest arr[val]
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            else:  # Both are Equal, Extract this info and put the intersection relationship in the O/P array
                # if nums1[i] not in intersection_array:       # If we Only wanna allow an Item only one time in the O/P
                #     intersection_array.append(nums1[i])
                intersection_array.append(nums1[i])
                i += 1  # Whenever The elements Match move both the indexes
                j += 1

        return intersection_array

# -----------------------------------------------------------------------------------------------------------
# 215. Kth Largest Element in an Array - Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

class Solution:             # Brute Force Approach - Tcol - O(N Log N), Scol - O(N)
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort()
        arr = nums[::-1]
        if k == 1:
            return arr[0]
        return arr[k - 1] if k - 1 else -1

#   Follow Up - Can you solve it without sorting?
# ```````````````````````````````````````````````` -- Min Heap Approach - Tcol - O(N log k), Scol - O(k)
import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        data = []
        heapq.heapify(data)
        for i in range(len(nums)):
            heapq.heappush(data, nums[i])
            if len(data) > k:
                heapq.heappop(data)
        return data[0]

# -----------------------------------------------------------------------------------------------------------
# 268. Missing Number - Input: nums = [9,6,4,2,3,5,7,0,1] Output: 8

class Solution:  # Brute Force Approach - Pythonic / Tcol - O(N*N), Space - O(1)
    def missingNumber_brute_Force(self, nums: list[int]) -> int:
        N = len(nums)
        for i in range(0, N + 1):
            if i not in nums:
                return i

                # Brute Force Approach - Language Independent / Tcol - O(N*N), Space - O(1)
    def missingNumber_brute_Force_2(self, nums: list[int]) -> int:
        N = len(nums)
        for i in range(N + 1):
            flag = 0
            for j in range(N):
                if nums[j] == i:
                    flag = 1
                    break
            if flag == 0:
                return i

                # Better Approach - Using A Single Hash Array, which keeps track of whats in the Original Arr.
    def missingNumber_Hash_Array_Optimal(self, nums: list[int]) -> int:  # And Marks Which element is not in the Orignl
        N = len(nums)
        hash_array = [0] * (N + 1)  # Tcol - O(2N)  /  Scol - O(N)
        for i in range(N):
            hash_array[nums[i]] = 1

        for i in range(len(hash_array)):
            if hash_array[i] == 0:
                return i

                # Optimal Solution 1 : Mathematical Soln. - Missing Num = (Sum of the first N Natural Numbers -
    def missingNumber(
        self, nums: list[int]
    ) -> int:  #                        Sum of the elements in the current Array)
        N = len(nums)
        Sum_of_the_first_N_Natural_Numbers = (
            N * (N + 1)
        ) // 2  # Tcol - O(N)  /  Scol - O(1)
        Sum_of_current_Array = sum(nums)
        return Sum_of_the_first_N_Natural_Numbers - Sum_of_current_Array

                # Optimal Solution 2 : XoR-ing Approach - (XOR of all the Numbers from 0 to N) ^
    def missingNumber(self, nums: list[int]) -> int:    # (XOR of all the numbers of nums array)
        N = len(nums)  # = Mising Number
        XOR1 = 0  # Tcol - O(2*N)
        for i in range(N + 1):       # Xoring Same Numbers Gives 0 -> 2 ^ 2 = 0
            XOR1 = (XOR1 ^ i)        # Xoring 0 and Any other number Gives that Number -> 0 ^ 2 = 2
                                     # In that Logic ~  1 , 2 , 3 , 4 , 5
        XOR2 = 0                     #                  ^   ^   ^   ^   ^
        for j in range(N):           #               ~  1 , 2 ,   , 4 , 5
            XOR2 = (XOR2 ^ nums[j])  #                  0 ^ 0 ^ 3 ^ 0 ^ 0  -->  3 (The Missing Number)
        return XOR1 ^ XOR2


# ----------------------------------------------------------------------------------------------------------------
# 485. Max Consecutive Ones - Given a binary array nums, return the maximum number of consecutive 1's in the array.
# nums = [1,1,0,1,1,1,0,0,1,1,0]   |    Output: 3

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        i = 0
        N = len(nums)
        max_count = float("-inf")
        temp = 0
        while i < N:
            if nums[i] != 1:
                max_count = max(max_count, temp)
                temp = 0
            else:
                temp += 1
            i += 1
        max_count = max(max_count, temp)
        return max_count

# ---------------------------------------------------------------------------------------------------------------
# 136. Single Number - Given a non-empty array of integers nums, every element appears twice except for one.
            # Find that single one. - Constant Space, and linear Time

nums = [4, 1, 2, 1, 2]
# Better Approach - Time Complexity: O(N), Space Col - O(N)
freq = {}
for n in nums:
    if n not in freq:
        freq[n] = 1
    elif n in freq:
        del freq[n]
# print(next(iter(freq)))

# Optimal Approach - Using XOR Logic -  Time Complexity: O(N), Space Col - O(1)
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        N = len(nums)  # Xoring Same Numbers Gives 0 -> 2 ^ 2 = 0
        single_num = nums[
            0
        ]  # Xoring 0 and Any other number Gives that Number -> 0 ^ 2 = 2
        for i in range(1, N):  # By that logic, For this - [1, 1, 2, 3, 3, 4, 4]
            single_num = (
                single_num ^ nums[i]
            )  # 1 ^ 1 = 0 | 4 ^ 4 = 0 | 3 ^ 3 = 0 | At last 0 ^ 2 = 2, We Return 2
        return single_num

# ---------------------------------------------------------------------------------------------------
# Problem Statement - Longest Subarray Whose Sum Is Equal To K (Array numbers are all positive) | 1 < nums[i] < 10^5
                # Given an array arr[] containing integers and an integer k, find the length of the longest subarray
                # where the sum of its elements is equal to the given value k. If there is no subarray sum = k, return 0.

# SubArray - Contiguous Part Of the Array | for Arr -[3, 6, 1, 3, 2, 1, 1, 1, 7], Subarrays include - [1,1,1], [6,1,3,2] etc.
# SubSequence - Non-Contiguous - for Arr -[3, 6, 1, 3, 2, 1, 1, 1, 7], SubSeqs include - [6,3,2], [1,1,1,1,7] etc.


def subArr_sum_eq_K_only_positive_numbers():  # Brute Force - With O(N^3) Time Complexity
    nums = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
    k = 3
    max_length = 0
    N = len(nums)
    for i in range(N):
        for j in range(i, N):
            curr_sum = 0
            for l in range(i, j + 1):
                curr_sum += nums[l]
            if curr_sum == k:
                print("here", i, j)
                max_length = max(max_length, j - i + 1)
    print(max_length)

def subArr_sum_eq_K_only_positive_numbers2():  # Brute Force 2 - With O(N^2) Time Complexity
    nums = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
    k = 3
    max_length = 0
    N = len(nums)
    for i in range(N):
        curr_sum = 0
        for j in range(i, N):
            curr_sum += nums[j]
            if curr_sum == k:
                print("here", i, j)
                max_length = max(max_length, j - i + 1)
    print(max_length)


def subArr_sum_eq_K_only_positive_numbers_Better_Solution():  # Better Solution - Using Hashing
    nums = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]        #  - With Time Complexity: O(N)   |   Space Complexity: O(N)
    k = 3
    N = len(nums)
    max_length = 0
    current_sum = 0
    pref_sum_hash_map = {}
    for i in range(N):
        current_sum += nums[i]
        if current_sum == k:
            max_length = max(max_length, i + 1)
        remainder = current_sum - k
        if remainder in pref_sum_hash_map:
            max_length = max(max_length, i - (pref_sum_hash_map[remainder]))
            
        if current_sum not in pref_sum_hash_map:
            pref_sum_hash_map[current_sum] = i

    print(max_length)


def subArr_sum_eq_K_only_positive_numbers_Optimal_Solution():  # Optimal Solution - Using Two Pointers
    nums = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]       #  - With Time Complexity: O(2N)   |   Space Complexity: O(1)
    k = 3
    N = len(nums)
    max_length = 0
    current_sum = nums[0]
    left = right = 0
    while right < N:
        while left <= right and current_sum > k:
            current_sum -= nums[left]
            left += 1
        if current_sum == k:
            max_length = max(max_length, right - left + 1)
        right += 1
        if right < N:
            current_sum += nums[right]
    return max_length

# ---------------------------------------------------------------------------------------------------
# Problem - Longest Subarray with Sum K - Given an array arr[] containing integers and an integer k. find 
        #   the length of the longest subarray where the sum of its elements is equal to the given value k.
        # Main Constraint is, This Time Array Will Have +ve's As well as -ve's in the Array

def subArr_sum_eq_K():                             #   [ -104 ≤ arr[i] ≤ 104 ]
    nums = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]          # Better Soln. - With Time Complexity: O(N)   |   Space Complexity: O(N)
    k = 3
    N = len(nums)
    max_length = 0
    sum = 0
    pref_sum_hash_map = {}
    for i in range(N):
        sum += nums[i]
        if sum == k:
            max_length = max(max_length, i + 1)
        remainder = sum - k
        if remainder in pref_sum_hash_map:
            max_length = max(max_length, i - (pref_sum_hash_map[remainder]))
            
        if sum not in pref_sum_hash_map:
            pref_sum_hash_map[sum] = i

    print(max_length)

# ---------------------------------------------------------------------------------------------------



        





