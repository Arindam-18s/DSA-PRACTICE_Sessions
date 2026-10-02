def print_name(i, n):
    if i > 5:
        return
    else:
        pass
        # print("seq")
        # print_name(i+1, n)    // But returning from recursion is not automatically backtracking.
if __name__ == "__main__":
    print_name(1, 5)
    
# ---------------------------------------------------------------------------------------------------
def print_name(i, n):
    if i < n:
        return
    else:
        pass
        # print(i)
        # print_name(i-1, n)
if __name__ == "__main__":
    print_name(5, 1)

# --------------------------------------------------------------------------------------------------
# i To N Using Backtracking - 1, 2, 3, 4, 5 (not using + to call the next iteration)
def sum_func(i, n):
    if i < 1:
        return
    else:
        sum_func(i - 1, n)
        # print(i)
if __name__ == "__main__":
    sum_func(5, 5)

# --------------------------------------------------------------------------------------------------
# N To i Using Backtracking - 5, 4, 3, 2, 1 (not using - to call the next iteration)
def sum_func(i, n):
    if i > n:
        return
    else:
        sum_func(i + 1, n)
        # print(i)
if __name__ == "__main__":
    sum_func(1, 5)

# --------------------------------------------------------------------------------------------------
# SUM OF Nums From 1 to N (Implementation of Head Recursion(Parameterized))

def print_name(no_of_iterations, sum):
    if no_of_iterations > 0:
        sum += no_of_iterations
        sum = print_name(no_of_iterations - 1, sum)     # Head Recursion
    return sum

if __name__ == "__main__":
    name = "seq"
    # print(print_name(5, 0))

# --------------------------------------------------------------------------------------------------
# SUM OF Nums From 1 to N (Implementation of Tail Recursion(Parameterized))

def sum_func(no_of_iterations, sum):
    if no_of_iterations < 0:
        return sum  # this is for the final N'th Case to go back to the very 1st Call
    return sum_func(no_of_iterations - 1, sum + no_of_iterations)

# if __name__ == "__main__":
#     print(sum_func(5, 0))

# --------------------------------------------------------------------------------------------------
# SUM OF Nums From 1 to N (Implementation Functional Recursion)

def functional(n):
    if n == 0:
        return n
    return n + functional(n - 1)   # 1 + 0, 2 + 1, 3 + 3, 4 + 6, 5 + 10, 

if __name__ == "__main__":
    pass
#     print(functional(5))

# --------------------------------------------------------------------------------------------------
# Factorial of N

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    pass
#     print(factorial(4))

# --------------------------------------------------------------------------------------------------
# Reversing an arr with Two pointers Recursion using L and R

def rev_arr(l, r):
    if l > r:
        return arr
    arr[l], arr[r] = arr[r], arr[l]
    return rev_arr(l + 1, r - 1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    rev_arr(0, len(arr) - 1)  # <- print to see the ans

# --------------------------------------------------------------------------------------------------
# Reversing an arr with one pointer i as Parameter Using Recursion(Technically gets the second pointer(n) from the main code black)

def arr_rev(i):
    if i > n // 2:
        return arr
    arr[i], arr[n - i] = arr[n - i], arr[i]     # Parameterized Recursion
    return arr_rev(i + 1)   # Search space is getting narrower and narrower from the front 

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    n = len(arr) - 1
    # print(arr_rev(0))

# --------------------------------------------------------------------------------------------------
# Check if a String is Pallindrome or not - Kinda like the prev Appr

def palindrome_str(i):
    if i > (n // 2):
        return True
    if str1[i] != str1[n - i]:
        return False
    return palindrome_str(i + 1)

if __name__ == "__main__":
    str1 = "ollo"
    n = len(str1) - 1
    # print(palindrome_str(0))

# --------------------------------------------------------------------------------------------------
# Fibonacci - Usage of Multiple Recursive Functions - Calls Happens sequencially, like F(n-1) will totally go until the base
# Case, come back with a value and then the f(n-2) will do the same

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    fibonacci(4)

# --------------------------------------------------------------------------------------------------
# LeetCode - 78 - Subset I - Pinting all the subsets of a given Array /List  - Timecol -> O((2^n) x n)

from typing import List
def print_subsequences(index, array: List, current_subseq_arr):
    if index >= len(array):
        # print(current_subseq_arr)
        return
    current_subseq_arr.append(array[index])
    print_subsequences(
        index + 1, array, current_subseq_arr
    )  # Take or pick the particular index into the subsequence

    current_subseq_arr.pop()  # remove the current element(backtrack)
    # Not Pick or not take condition, this element is not added to your subsequence
    print_subsequences(index + 1, array, current_subseq_arr)

if __name__ == "__main__":
    arr1 = [3, 1, 2]
    print_subsequences(0, arr1, [])

# --------------------------------------------------------------------------------------------------
# Printing SubSequences Whose Sum is K

def subSeq_sum_equalsK(
    index, current_subarray: List, current_indexes: List, current_sum
):
    if index == len(array):
        if current_sum == k:
            pass
            # print(current_subarray)
            # print(current_indexes)  #Special Case for index printing
        return

    current_subarray.append(array[index])
    # current_indexes.append(index)   #Special Case for index printing
    current_sum += array[index]
    subSeq_sum_equalsK(index + 1, current_subarray, current_indexes, current_sum)

    # current_indexes.pop()           #Special Case for index printing
    current_sum -= current_subarray.pop()  # Two lines merged
    subSeq_sum_equalsK(index + 1, current_subarray, current_indexes, current_sum)

if __name__ == "__main__":
    array = [1, 4, 7, 2, 3]
    k = 5
    # subSeq_sum_equalsK(0, [], [], 0)

# --------------------------------------------------------------------------------------------------
# Printing SubSequences Whose Sum is K - Only 1 Output

def Subseq_sum_equals_k_printing_1_output(index, current_subseq, current_sum, ans):
    if index == len(nums):
        if current_sum == k:
            ans.append(current_subseq.copy())
            return True
        return False

    current_subseq.append(nums[index])
    current_sum += nums[index]
    if (Subseq_sum_equals_k_printing_1_output(index + 1, current_subseq, current_sum, ans) == True):
        return True
    current_sum -= current_subseq.pop()
    if (Subseq_sum_equals_k_printing_1_output(index + 1, current_subseq, current_sum, ans) == True):
        return True
    return False

if __name__ == "__main__":
    nums = [1, 3, 8, 4, 9, 2, 6]
    k = 10
    ans = []
    print(Subseq_sum_equals_k_printing_1_output(0, [], 0, ans))
    print(ans)

# --------------------------------------------------------------------------------------------------
# Total Count of SubSequences Whose Sum is == K

def Subseq_sum_equals_k_printing_1_output(
    index, current_subseq: List, current_sum: int
):
    if index == len(array):
        if current_sum == k:
            print(current_subseq)
            return 1
        return 0

    current_subseq.append(array[index])
    current_sum += array[index]
    Take_count = Subseq_sum_equals_k_printing_1_output(
        index + 1, current_subseq, current_sum
    )

    current_sum -= current_subseq.pop()
    NotTake_count = Subseq_sum_equals_k_printing_1_output(
        index + 1, current_subseq, current_sum
    )
    return Take_count + NotTake_count

if __name__ == "__main__":
    array = [8, 5, 9, 1, 7, 2, 3]
    k = 10
    # print(Subseq_sum_equals_k_printing_1_output(0, [], 0))

# --------------------------------------------------------------------------------------------------
# Merge Sort Recursion - Tcol - O(nLogn) Scol - O(n)

def merge(array, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if array[left] <= array[right]:
            temp.append(array[left])
            left += 1
        else:
            temp.append(array[right])
            right += 1
    while left <= mid:
        temp.append(array[left])
        left += 1
    while right <= high:
        temp.append(array[right])
        right += 1
    # print(temp)
    for i in range(low, high + 1):
        array[i] = temp[i - low]
    return array

def merge_sort_recursion(array, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort_recursion(array, low, mid)
    merge_sort_recursion(array, mid + 1, high)
    merge(array, low, mid, high)
    return array

if __name__ == "__main__":
    array = [9, 4, 7, 1, 2, 5, 6, 3]
    (merge_sort_recursion(array, 0, len(array) - 1))

# --------------------------------------------------------------------------------------------------
# Quick Sort Recursion - Tcol - O(nLogn) Scol - O(n)

def setting_pivot_at_the_right_place(nums, low, high):
    pivot = nums[low]
    i, j = low, high
    while i < j:
        while nums[i] <= pivot and i < high:   #Everything is fine, go on
            i += 1
        while nums[j] > pivot and j > low:     #Everything is fine, go on
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j

def QuickSort(nums, low, high):
    if low < high:
        partition_idx = setting_pivot_at_the_right_place(nums, low, high)
        QuickSort(nums, low, partition_idx - 1)
        QuickSort(nums, partition_idx + 1, high)
    return nums

if __name__ == "__main__":
    nums = [4, 6, 2, 5, 7, 9, 1, 3]
    # print(QuickSort(nums, 0, len(nums) - 1))

# --------------------------------------------------------------------------------------------------
# Printing Sums all the individual subsequences of a given Array /List

def subset_sum_I(index, arr, current_subarray, current_sum, output):
    if index >= len(arr):
        output.append(current_sum)
        return

    current_subarray.append(arr[index])
    current_sum += arr[index]
    subset_sum_I(index + 1, arr, current_subarray, current_sum, output)

    current_sum -= current_subarray.pop()
    subset_sum_I(index + 1, arr, current_subarray, current_sum, output)
    return output

if __name__ == "__main__":
    arr = [3, 1, 2]
    # print(subset_sum_I(0, arr, [], 0, []))

# --------------------------------------------------------------------------------------------------
# 90. Subsets II - Input: nums = [1,2,2] Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# May Contain Duplicate values in a subset, but not duplicates subsets

def subsets_II(index, arr, current_subarray, output):
    output.append(current_subarray.copy())

    for i in range(index, len(arr)):
        if i != index and arr[i] == arr[i - 1]:
            continue

        current_subarray.append(arr[i])
        subsets_II(i + 1, arr, current_subarray, output)

        current_subarray.pop()
    return output

if __name__ == "__main__":
    arr = [3, 1, 2, 2]
    arr.sort()
    # print(subsets_II(0, arr, [], []))

# --------------------------------------------------------------------------------------------------
# 46. Permutations - Input: nums = [1,2,3] Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# For(Lists and Strings)

def permutations(current_array):
    # We have selected enough elements
    if len(current_array) == len(array):
        print(current_array)
        return

    for curr in array:  # Try every element as the NEXT element
        # Don't use an element twice
        if curr not in current_array:
            current_array.append(curr)  # CHOOSE
            permutations(current_array)  # GO DEEPER
            current_array.pop()  # UNDO

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    # permutations([])

def permutation_string(current_string_permutation, output):
    if len(current_string_permutation) == len(string):
        output.append("".join(current_string_permutation))
        return
    for s in string:
        if s not in current_string_permutation:
            current_string_permutation.append(s)
            permutation_string(current_string_permutation, output)
            current_string_permutation.pop()
    return output

if __name__ == "__main__":
    string = "abcde"
    # print(permutation_string([], []))

# --------------------------------------------------------------------------------------------------
# 47. Permutations II - Input: nums = [1,1,2] Output: [[1,1,2], [1,2,1], [2,1,1]]
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

class Solution:
    def all_possible_with_duplicates(self, nums, current_permutation, output, used):
        if len(current_permutation) == len(nums):
            output.append(current_permutation.copy())
            return

        for i in range(len(nums)):
            if used[i]:  # Have we already used this index?
                continue
            if (
                i > 0 and nums[i] == nums[i - 1] and not used[i - 1]    #<-- (used[i - 1] This is not a condition, this is an array, which contains, values like [True, False, False, True] 
            ):  # Skip duplicate choices at the same level
                continue

            used[i] = True
            current_permutation.append(nums[i])
            self.all_possible_with_duplicates(nums, current_permutation, output, used)
            current_permutation.pop()
            used[i] = False
        return output

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        used = [False] * len(nums)
        return self.all_possible_with_duplicates(nums, [], [], used)

# --------------------------------------------------------------------------------------------------
# 3483. Unique 3-Digit Even Numbers - Input: digits = [1,2,3,4] Output: 12 - ** SAME TO SAME PERMUTATION Problem **
# The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. 
                                                # Note that 222 cannot be formed because there is only 1 copy of the digit 2.
class Solution:
    def subseq_with_no_leading_zeroes(self, digits, current_subseq, ans, used):
        if len(current_subseq) == 3:
            if current_subseq[0] != 0 and current_subseq[2] % 2 == 0:
                ans[0] += 1
            return
        for i in range(len(digits)):
            if used[i]:
                continue
            if i > 0 and digits[i] == digits[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            current_subseq.append(digits[i])
            self.subseq_with_no_leading_zeroes(digits, current_subseq, ans, used)
            current_subseq.pop()
            used[i] = False
        return ans
    
    def totalNumbers(self, digits: List[int]) -> int:
        if not digits or len(digits) <= 2:
            return 0
        digits.sort()
        used = [False] * len(digits)
        res = self.subseq_with_no_leading_zeroes(digits, [], [0], used)
        return res[0]

# --------------------------------------------------------------------------------------------------
# 22. Generate Parentheses - Same Permutations BackTracking Intuition -> Time - O(4^n / sqrt(n)); Space - O(n)
                           # Main Intuition -                         -> We can add ( as long as open < n. 
                                                                     #-> We can add ) only when close < open
def permutations(open, close, n, current_perm, output):
    if len(current_perm) == 2 * n:
        output.append(current_perm)
        return
    if open < n:
        permutations(open + 1, close, n, current_perm + "(", output)
    if close < open:
        permutations(open, close + 1, n, current_perm + ")", output)
    return output

if __name__ == "__main__":
    n = 3
    # Output: ["((()))","(()())","(())()","()(())","()()()"]
    print(permutations(0, 0, n, "", []))

# --------------------------------------------------------------------------------------------------
# 51. N-Queens

def Nqueens_solve(self, column_num, n, board, leftRow, leftUpperDiagonal, leftLowerDiagonal, ans):
    if column_num == n:
        ans.append(["".join(row) for row in board])
        return

    for row in range(n):
        if (
            leftRow[row] == 0
            and leftUpperDiagonal[row + column_num] == 0
            and leftLowerDiagonal[n - 1 + column_num - row] == 0
        ):
            board[row][column_num] = "Q"
            leftRow[row] = 1
            leftUpperDiagonal[row + column_num] = 1
            leftLowerDiagonal[n - 1 + column_num - row] = 1

            self.Nqueens_solve(
                column_num + 1, n, board, leftRow, leftLowerDiagonal, leftUpperDiagonal, ans
            )
            board[row][column_num] = "."
            leftRow[row] = 0
            leftUpperDiagonal[row + column_num] = 0
            leftLowerDiagonal[n - 1 + column_num - row] = 0
    return ans

if __name__ == "__main__":
    n = 4
    board = [["." for i in range(n)] for j in range(n)]
    leftRow = [0] * n
    leftUpperDiagonal = [0] * (2 * n - 1)
    leftLowerDiagonal = [0] * (2 * n - 1)
    # print(Nqueens_solve(0, n, board, leftRow, leftUpperDiagonal, leftLowerDiagonal, []))

# --------------------------------------------------------------------------------------------------
# 131. Palindrome Partitioning

class Solution:
    def is_pallindrome(self, s, start, end):
        substr = s[start:end + 1]
        if substr == substr[::-1]:
            return True
        return False

    def no_of_partitions(self, index, s, path, ans):
        if index == len(s):
            ans.append(path.copy())
            return
        for i in range(index, len(s)):
            if self.is_pallindrome(s, index, i):
                path.append(s[index:i+1])
                self.no_of_partitions(i + 1, s, path, ans)
                path.pop()
        return ans
    
    def partition(self, s: str) -> list[list[str]]:
        if not s:
            return [[""]]
        return self.no_of_partitions(0, s, [], [])
        
# --------------------------------------------------------------------------------------------------
# LeetCode - 60 K-th Permutation(Permutation Sequence)

class Solution:
    def k_th_permutation(self, nums, used, current_permutation, counter, k):
        if len(current_permutation) == len(nums):
            counter[0] += 1
            if counter[0] == k:
                return "".join(current_permutation)
            return None

        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            used[i] = True
            current_permutation.append(nums[i])
            res = self.k_th_permutation(nums, used, current_permutation, counter, k)    # Capture the result from the deeper call
            if res: 
                return res
            current_permutation.pop()
            used[i] = False
    
    def getPermutation(self, n: int, k: int) -> str:
        if n <= 1:
            return f"{n}"
        used = [False] * n
        nums = [str(i + 1) for i in range(n)] 
        counter = [0]
        return self.k_th_permutation(nums, used, [], counter, k)

# --------------------------------------------------------------------------------------------------
# 77. Combinations -  Input: n = 4, k = 2 Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

class Solution:
    def combinations(self, index, nums, k, current_combination, ans):
        if len(current_combination) == k:
            ans.append(current_combination.copy())
            return
        while index < len(nums):
            current_combination.append(nums[index])
            self.combinations(index + 1, nums, k, current_combination, ans)
            current_combination.pop()
            index += 1
        return ans

    def combine(self, n: int, k: int) -> list[list[int]]:
        if n <=1 :
            return [[1]]
        if k == 1:
            return [[i + 1] for i in range(n)]
        nums = [i+1 for i in range(n)]
        return self.combinations(0, nums, k, [], [])
# --------------------------------------------------------------------------------------------------
# 216. Combination Sum III - Input: k = 3, n = 9 Output: [[1,2,6],[1,3,5],[2,3,4]]

class Solution:
    def valid_combinations(self, index, nums, k, n, current_combination, current_sum, ans):
        if len(current_combination) == k and current_sum == n:
            ans.append(current_combination.copy())
            return

        while(index < len(nums)):
            current_combination.append(nums[index])
            current_sum += nums[index]
            self.valid_combinations(index + 1, nums, k, n, current_combination, current_sum, ans)
            current_sum -= current_combination.pop()
            index += 1
        return ans

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        temp_sum = 0
        for i in range(k):
            temp_sum += i+1
        if n < temp_sum:
            return []
        nums = [i+1 for i in range(9)]

        return self.valid_combinations(0, nums, k, n, [], 0, [])
# --------------------------------------------------------------------------------------------------
