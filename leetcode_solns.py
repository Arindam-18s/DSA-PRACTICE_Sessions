# Two SUM
seen = {}  # will store {value: index}

for i, num in enumerate(nums):
    complement = target - num  # For each number, check if its "complement" (the number needed to reach the target) 
    if complement in seen:     # has already been seen.If yes, you found your pair. If no, 
        print [seen[complement], i] # remember this number's value and index for future checks.
    seen[num] = i
# -------------------------------------------------
# Palindrome
class Solution(object):
    def isPalindrome(self, x):
        num = x
        num_str = str(num)
        rev = num_str[::-1]

        return num_str == rev

# -------------------------------------------------
#Roman to Integer

s = "LXXIX"
roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}   # HashMap(dictionary)
total = 0
# print(len(s))

for i in range(len(s)):
        # Check if the current value is less than the next value
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:      # i + 1 < len(s) <- short-circuit evaluation.
            total -= roman_map[s[i]]  # Subtractive rule
        else:
            total += roman_map[s[i]]  # Additive rule

SUM  = 50 + 10 + 10 - 1 + 10
# print(SUM)

# -------------------------------------------------
# Longest Common Prefix - both code wil work

import os
strings = ["global", "glossary", "glove"]

common = os.path.commonprefix(strings)
# print(f"Strings match up to position {len(common)}. Common part: '{common}'")

#~~~~~~~~

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        # 1. Use a safer name like 'base_str' instead of 'str'
        base_str = strs[0]
        
        # 2. Loop through each character index of the first string
        for i in range(len(base_str)):
            char_to_check = base_str[i]
            
            # 3. Check this position against all other strings
            for other_str in strs[1:]:
                # If the other string is out of bounds, OR the character mismatches
                if i >= len(other_str) or other_str[i] != char_to_check:
                    # Return the valid prefix we built up until index 'i'
                    return base_str[:i]
                
# -------------------------------------------------                    
# Longest Substring Without Repeating Characters - leetcode - 3

s = "1R1T7"
char_list = list(s)  
answer = []
ans = 0
final_ans = 0

for char in char_list:  
    if char not in answer: 
        answer.append(char)
        ans = len(answer)
        if ans > final_ans:
            final_ans = ans
    else:
        idx = answer.index(char)
        answer = answer[idx + 1:]
        answer.append(char)

print(final_ans)
# -------------------------------------------------    
# Reverse Integer

class Solution(object):
    def reverse(self, x):
        while(x % 10 == 0):
            x = x // 10  # Chop off the last zero
        
        if x >= 0:              # Convert to string, reverse it, convert back to int
            return int(str(x)[::-1])
        else:
            return -int(str(abs(x))[::-1])      # For negative numbers, slice the absolute value and add the minus back
# -------------------------------------------------    
# 206. Reverse Linked List      

class Solution(object):
    def reverseList(self, head):
        cur = head
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev
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
# 3658. GCD of Odd and Even Sums

class Solution(object):
    def gcdOfOddEvenSums(self, n):
        SumOdd = 0
        SumEven = 0
    
        current_odd = 1             # Track the actual numbers to add
        current_even = 2
        
        for i in range(n):          # Loop exactly n times to grab the first n numbers
            SumOdd += current_odd
            current_odd += 2  # Move to next odd: 1 -> 3 -> 5 -> 7
            
            SumEven += current_even
            current_even += 2 # Move to next even: 2 -> 4 -> 6 -> 8
            
        b = SumEven
        a = SumOdd
        while b:
            a, b = b, a % b
        return a
# ------------------------------------------------- 
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
# 3754. Concatenate Non-Zero Digits and Multiply by Sum I 

n = 1000
i = 0
sum = 0
x = 0
while ( n > 0) :
    rem = n % 10
    if(rem != 0):
        sum = sum + rem
        x = x + pow(10, i) * rem        #concatenating
        i = i + 1 
    n = n // 10

mul = sum * x
print(mul)
# ------------------------------------------------- 
# 66. Plus One <- Input: digits = [9] Output: [1,0] | Input: digits = [4,3,2,1] Output: [4,3,2,2]

class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        
        for i in range(n - 1, -1, -1):          # Move backwards from the last digit to the first
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0               # If it is a 9, change it to 0 and continue the loop
            
        return [1] + digits       # If the loop finishes, all digits were 9s (e.g., [9, 9] ->) We must add a 1 at the front
# ------------------------------------------------- 
# 238. Product of Array Except Self

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        l_mult = 1
        r_mult = 1
        L_array = [0] * n
        R_array = [0] * n

        for i in range(n):
            j = -i -1
            L_array[i] = l_mult
            R_array[j] = r_mult
            l_mult = l_mult * nums[i]
            r_mult = r_mult * nums[j]

        result = []
        for i in range(len(L_array)):
            result.append(L_array[i]*R_array[i])
        return result
# ------------------------------------------------- 
# 121. Best Time to Buy and Sell Stock

class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_price = float('inf')
        
        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price

            if profit > max_profit:
                max_profit = profit
        return max_profit
#------------------------------------------------- 
# 2. Add Two Numbers
class ListNode(object):
    def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        cur = dummy

        carry = 0
        while(l1 or l2 or carry):
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next

        return dummy.next

# ------------------------------------------------- 
# leetcode - 78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return result
# ------------------------------------------------- 
# 3536. Maximum Product of Two Digits 

class Solution:
    def maxProduct(self, n: int) -> int:
        nums = [int(d) for d in str(n)]
        second_max = sorted(nums)[-2]
        max = sorted(nums)[-1]
        multi = max * second_max
        return multi

# second_max = sorted(set(n))[-2]       <- for sorted o/p
# max = sorted(set(n))[-1]

# ------------------------------------------------- 
# 628. Maximum Product of Three Numbers

nums = [-1,-2, 3, -3 ,-4, 5, 7, 9, 10]
    
max1 = max2 = max3 = float('-inf')
min1 = min2 = float('inf')

for num in nums:
    if num > max1:
        max3 = max2
        max2 = max1
        max1 = num
    elif num > max2:
        max3 = max2
        max2 = num
    elif num > max3:
        max3 = num

    if num < min1:
        min2 = min1
        min1 = num
    elif num < min2:
        min2 = num

print(max(max1 * max2 * max3,max1 * min1 * min2))
# ------------------------------------------------- 
# 100. Same Tree

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both nodes are None -> structurally identical at this branch
        if not p and not q:
            return True
            
        # One is None and the other isn't, or their values don't match
        if not p or not q or p.val != q.val:
            return False
            
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# ------------------------------------------------- 
# 42. Trapping Rain Water  
 
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]

        while(left < right):
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])

            if(max_left < max_right):
                water += max_left - height[left]
                left +=1
            else:
                water += max_right - height[right]
                right -=1
         
        return water

# ------------------------------------------------- 
# 102. Binary Tree Level Order Traversal

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        q = deque()
        q.append(root)
        ans = []

        while q:
            level = []
            n = len(q)   # cause q stores all the upcoing level elemnents

            for i in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)

        return ans
# ------------------------------------------------- 
# 202. Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
            
        return False

    def sumOfSquares(self, n : int) -> int:
            output = 0

            while n:
                digit = n % 10
                digit = digit ** 2
                output += digit
                n = n // 10
            return output

# ------------------------------------------------- 
# 507. Perfect Number
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if (num == 1):
            return False

        sum = 1
        square_root = int(num ** 0.5)

        for i in range(2, square_root + 1):
            if num % i == 0:
                sum += i + (num // i)

        return (sum == num)

# ------------------------------------------------- 
# prime using recursion
def is_prime(n,i):      # is_prime(n, m-1)
    if i == 1:
        return True
    if n % i == 0:      # means compleatly divisible
        return False
    return is_prime(n, i-1) 
    
n = int(input("enter a number to check prime : "))
prime = is_prime(n,n-1)     # e.g. n = 11, i = 10 and i will check until it becomes 1
if prime is True:
    print("prime")
else:
    print("not prime")
# ------------------------------------------------- 
# fibonacci
def fibonacci(num):
    if num == 0:
        return False

    output = [0, 1]
    i = 0
    j = 1

    for i in range(num):
        first = output[i]
        second = output[j]
        output.append(first + second)
        j += 1

    return output
    
arr = fibonacci(20)
print(arr)
# ------------------------------------------------- 
#leaders in an array
nums = [7, 10, 4, 10, 6, 5, 2]
ans = []
max = 0

for n in range(len(nums) - 1, -1, -1):
    if nums[n] > max:
        if nums[n] not in ans:
            ans.append(nums[n])
            max = nums[n]

ans.reverse()
print(ans)
# ------------------------------------------------- 
# 34. Find First and Last Position of Element in Sorted Array - must be O(log n) runtime complexity.- Use Binary Search

class Solution:
    def findStartingIndex (self, nums: List[int], target: int) -> int:
        index = -1
        start = 0
        end = len(nums) - 1

        while(start <= end):
            midpoint = start + (end - start) // 2

            if nums[midpoint] >= target:
                end = midpoint - 1
            else:
                start = midpoint + 1

            if nums[midpoint] == target:
                index = midpoint
        return index

    def findEndingIndex (self, nums: List[int], target: int) -> int:
        index = -1
        start = 0
        end = len(nums) - 1
        
        while(start <= end):
            midpoint = start + (end - start) // 2
            if nums[midpoint] <= target:
                start = midpoint + 1
            else:
                end = midpoint - 1

            if nums[midpoint] == target:
                index = midpoint
        return index
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1] 
        result[0] = self.findStartingIndex(nums, target)
        result[1] = self.findEndingIndex(nums, target)

        return result

# ------------------------------------------------- 
# 21. Merge Two Sorted Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next

# ------------------------------------------------- 
# 128. Longest Consecutive Sequence - Input: nums = [100,4,200,1,3,2]  Output: 4

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while(n + length) in numSet:
                    length +=1
                longest = max(length, longest)
        return longest

nums = [100,4,200,1,3,2]
sol = Solution()
ans = sol.longestConsecutive(nums)
print(ans)

# ------------------------------------------------- 
# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapForMatching = {")" : "(", "]" : "[", "}" : "{"}

        for char in s:
            if char in mapForMatching:
                if stack and stack[-1] == mapForMatching[char]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(char)
        return True if not stack else False

# ------------------------------------------------- 
# 3675. Minimum Operations to Transform String

class Solution:
    def minOperations(self, s: str) -> int:
        res = 0
        string = list(s)
        for n in string:
            ch = n
            if ch == "a":
                continue
            dis = (ord('z') - ord(ch)) + 1
            res = max(res, dis)
        return res

# ------------------------------------------------- 
# 287. Find the Duplicate Number - no extra space, contant time soln. - using floyds cyclic algo

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow  = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

# ------------------------------------------------- 
# 41. First Missing Positive - using cycic sort

from typing import List
nums = [4, 2, 9, 0, 1, 3, 8]

def smallest_missing_positive(nums: List[int]):
    n = len(nums)
    i = 0
    while i < n:
        correct = nums[i] - 1

        if ( 1 <= nums[i] <= n and nums[i] != nums[correct]):
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i+1
    return n + 1

missing = smallest_missing_positive(nums)
print(missing)

# ------------------------------------------------- 
# Two-wheeler/four-wheeler production planning - given total vehicle count and total wheel count / how many of each type were made

def two_four_wheelers(V: int, W: int):
    if W % 2 != 0 or W < 2 * V or W > 4 * V:
        print("INVALID INPUT")
        return

    four_wheelers = (W - 2 * V) // 2
    two_wheelers = V - four_wheelers

    print("two wheelers = ", two_wheelers)
    print("four wheelers = ", four_wheelers)
two_four_wheelers(10, 28)

# ------------------------------------------------- 
# Grid path counting - count distinct paths from one corner of a grid to another under movement constraints. 
def grid_paths(n, m):
    if n == 1 or m ==1:
        return 1
    else:
        return grid_paths(n - 1, m) + grid_paths(n, m - 1)
print(grid_paths(3, 3))

# ------------------------------------------------- 
# Write a function that counts the number of ways you  can partition n objects using parts upto n(assuming m > 0)

def count_partitions(n, m):
    if n == 0:
        return 1
    elif m == 0 or n < 1:
        return 0
    else:
        return count_partitions(n - m, m) + count_partitions(n, m - 1)
print(count_partitions(6, 4))

# ------------------------------------------------- 
# 2390. Removing Stars From a String

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                stack and stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
# ------------------------------------------------- 
# printing prime till N - using the sieve of Eratosthenes - O(N log log N) which is < normal methods O(N x sqrt(N))

def sieve_of_eratosthenes(n):
    prime = [True for _ in range(n + 1)]
    prime[0] = prime[1] = False  
    
    p = 2
    while (p * p <= n):
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return [i for i in range(2, n + 1) if prime[i]]

print(sieve_of_eratosthenes(30))   # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# ------------------------------------------------- 
# 3731. Find Missing Elements

nums = [7,8,6,10,3,9]
smallest = min(nums)
largest = max(nums)
ans = []
hashh = set()

for i in range(smallest, largest + 1):
    hashh.add(i)

for n in hashh:
    if n not in nums:
        ans.append(n)
print(ans)
# ------------------------------------------------- 
# leetcode - 1636 - Sort array by increasing frquency

from collections import Counter
nums = [-1,1,-6,4, 4, 5,-6,1,4,1]
    
count = Counter(nums)

def custom_sort(n):
    return (count[n], -n)

nums.sort(key = custom_sort)
print(nums)
# ------------------------------------------------- 
# 198. House Robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for n in nums:
            # temp is the max money up to the current house
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
# ------------------------------------------------- 
# leetcode - 3345. Smallest Divisible Digit Product I

n = 15
t = 3

def check(n, t):
    while True:
        product = 1
        num = n
        while(num):
            temp = num % 10
            product *= temp
            num = num // 10

        if product % t == 0:
            return n
        else:
            n +=1

print(check(n, t))
# ------------------------------------------------- 
# 53. Maximum Subarray - nums = [-2,1,-3,4,-1,2,1,-5,4] - o/p -> ([4, -1, 2, 1], 6)

from typing import List
nums = [-2,1,-3,4,-1,2,1,-5,4]

def subarr(nums: List[int]):
    sum = 0
    max_sum = float('-inf')
    ans = []
    best_ans = []
    for n in nums:
        if sum < 0:
            sum = n
            ans = [n]
        else:
            sum += n
            ans.append(n)
        if sum > max_sum:
            max_sum = sum
            best_ans = ans.copy()

    return best_ans, max_sum
        
print(subarr(nums))
# ------------------------------------------------- 
# 191. Number of 1 Bits - Input: n = 128 / Output: 1 - The input binary string 10000000 has a total of one set bit.

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0:
            ans += 1
            n = n & (n-1)
        return ans
# ------------------------------------------------- 
# 338. Counting Bits - Input: n = 5Output: [0,1,1,2,1,2],Explanation: 0 --> 0 1 --> 1 2 --> 10 3 --> 11 4 --> 100 5 --> 101

from typing import List

def find(n:str)-> List[int]:
    num = int(n)
    ans = []
    for n in range(num + 1):
        temp = 0
        while(n != 0):
            temp += 1
            n = n & (n-1)
        ans.append(temp)
    return ans

print(find("20"))
# ------------------------------------------------- 
# 268. Missing Number - Input: nums = [9,6,4,2,3,5,7,0,1] Output: 8

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        return res

# ------------------------------------------------- 
# 190. Reverse Bits - I/p: n = 43261596 O/p: 964176192 00000010100101000001111010011100 -> 00111001011110000010100101000000

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res

# ------------------------------------------------- 
# 70. Climbing Stairs - i/p - 5 / o/p - 8

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n ==1:
            return 1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return (dp[n - 1])

# ------------------------------------------------- 
# 322. Coin Change - Input: coins = [1,2,5], amount = 11 Output: 3 Explanation: 11 = 5 + 5 + 1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

# ------------------------------------------------- 
# 300. Longest Increasing Subsequence - Input: nums = [0,1,0,3,2,3] Output: 4

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return []

        last = len(nums) - 1
        ans = [nums[last]]
        
        while last > 0:
            current_val = nums[last - 1]
            if current_val < ans[-1]:
                ans.append(current_val)
            else:
                for i in range(len(ans)):
                    if current_val >= ans[i]:
                        ans[i] = current_val
                        break
            last -= 1
        return len(ans)

# ------------------------------------------------- 
# leetcode 647. Palindromic Substrings - Input: s = "aaa" Output: 6 | "a", "a", "a", "aa", "aa", "aaa".

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res

# ------------------------------------------------- 
# 349. Intersection of Two Arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()
        point1 = point2 = 0
        ans = set()

        while point1 < len(nums1) and point2 < len(nums2):
            if nums1[point1] == nums2[point2]:
                ans.add(nums1[point1])
                point1 += 1
                point2 += 1
            elif nums1[point1] < nums2[point2]:
                point1 += 1
            else:
                point2 += 1
        return list(ans)

# ------------------------------------------------- 
# 2095. Delete the Middle Node of a Linked List

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        curr = head
        prev = None
            
        while curr is not None:
            count += 1
            curr = curr.next
        
        if count <= 1:
            return None

        curr = head
        middle = count // 2
        curr_index = 0

        while curr is not None:
            if curr_index == middle:
                prev.next = curr.next
                return head
            else:
                curr_index +=1
                prev = curr
                curr = curr.next  

# ------------------------------------------------- 
# 3090. Maximum Length Substring With Two Occurrences - Input: s = "bcbbbcba" Output: 4 / Sliding Window

from collections import defaultdict
s = "bcbbbcba"
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        p1 = 0
        max_len = 0
        for p2 in range(len(s)):            # p2 expands the window forward linearly
            freq[s[p2]] += 1
            while freq[s[p2]] > 2:          # 🟩 If a character occurs more than twice, shrink from the left
                freq[s[p1]] -= 1
                p1 += 1  # Move left pointer forward
                
            current_window_len = p2 - p1 + 1        # Calculate the current valid window length
            if current_window_len > max_len:
                max_len = current_window_len
        return max_len,freq

sol = Solution()
ans = sol.maximumLengthSubstring(s)
print("Maximum unique character count in valid window:", ans)

# ------------------------------------------------- 
# 409. Longest Palindrome  -- Input: s = "abccccdd" Output: 7

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_counts = Counter(s)
        ans = 0
        has_odd = False
        
        # Step 2: Sum up lengths
        for count in char_counts.values():
            if count % 2 == 0:
                ans += count
            else:
                ans += count - 1  
                has_odd = True    
        
        return ans + 1 if has_odd else ans
solver = Solution()
print(solver.longestPalindrome(s = "abccccdd"))

# ------------------------------------------------- 
# 904. Fruit Into Baskets - Input: fruits = [1,2,3,2,2] Output: 4

from collections import defaultdict
trees = [1,2,3,2,2]
basket = defaultdict(int)
max_fruits = 0
left = 0

for right in range(len(trees)):
    curr = trees[right]
    basket[curr] += 1
    
    while len(basket) > 2:
        left_fruit = trees[left]
        basket[left_fruit] -= 1  
        
        if basket[left_fruit] == 0:
            del basket[left_fruit]
        left += 1  
    current_window_size = right - left + 1
    max_fruits = max(max_fruits, current_window_size)
print(max_fruits)  

# ------------------------------------------------- 
# 209. Minimum Size Subarray Sum - Input: target = 7, nums = [2,3,1,2,4,3] Output: 2

target = 7
nums = [2,3,1,2,4,3]
low = 0
min_len_window = float('inf')
temp_sum = 0

for high in range(len(nums)):
    temp_sum += nums[high]
    while(temp_sum >= target):
        current_window = high - low + 1
        min_len_window = min(min_len_window, current_window)

        temp_sum -= nums[low]
        low += 1

print(min_len_window)

# ------------------------------------------------- 
# 3702. Longest Subsequence With Non-Zero Bitwise XOR - Input: nums = [1,2,3] Output: 2

nums = [1,2,3]
total_xor = 0
has_nonZero = False
k = len(nums)

for n in range(k):
    total_xor ^= nums[n]
    if nums[n] != 0:
        has_nonZero = True

if total_xor != 0:
    print(k)
elif has_nonZero:
    print(k - 1)
else:
    print(0)
# ------------------------------------------------- 
# 560. Subarray Sum Equals K / prefix sum implementation
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        curSum = 0
        prefixSum = { 0 : 1 }
        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        return res

# ------------------------------------------------- 
# 303. Range Sum Query - Immutable / prefix sum implementation

class NumArray:
    def __init__(self, nums: List[int]):
        self.pref_sum = list(nums)
        for i in range(1, len(nums)):
            self.pref_sum[i] += self.pref_sum[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        rightPointer = self.pref_sum[right]
        leftPointer = self.pref_sum[left - 1] if left > 0 else 0
        return rightPointer - leftPointer

# ------------------------------------------------- 
 # 35. Search Insert Position - Binary Search

nums = [1,3,5,6]
target = 5
l = 0
r = len(nums) - 1
while(l <= r):
    middle = (l + r) // 2
    if nums[middle] == target:
        print(middle)
        break
    elif target < nums[middle]:
        r = middle - 1
    else:
        l = middle + 1
# ------------------------------------------------- 
# 33. Search in Rotated Sorted Array - Binary Search

nums = [4,5,6,7,0,1,2]
target = 0
l = 0
r = len(nums) - 1
while(l <= r):
    middle = (l + r) // 2
    if nums[middle] == target:
        print(middle)
    if nums[l] <= nums[middle]:
        if nums[l] <= target < nums[middle]:
            r = middle - 1
        else:
            l = middle + 1
    else:
        if nums[middle] < target <= nums[r]:
            l = middle + 1
        else:
            r = middle - 1
print(-1)
# ------------------------------------------------- 
# 34. Find First and Last Position of Element in Sorted Array  -- Input: nums = [5,7,7,8,8,10], target = 8 Output: [3,4]

nums = [5,7,7,7,8,8,8,8,8,8,8,8,8,10]
target = 8

l = 0
r = len(nums) - 1
first_occ = 0
last_occ = 0
num = -1

while(l <= r):
    middle = (l + r) // 2
    if nums[middle] == target:
        first_occ = middle
        num = nums[middle]
        r = middle - 1
    elif target < nums[middle]:
        r = middle - 1
    else:
        l = middle + 1

while(l <= r):
    middle = (l + r) // 2
    if nums[middle] == target:
        last_occ = middle
        num = nums[middle]
        l = middle + 1
    elif target < nums[middle]:
        r = middle - 1
    else:
        l = middle + 1

print(first_occ, num)
print(last_occ, num)
# ------------------------------------------------- 
# 852. Peak Index in a Mountain Array  -  Input: arr = [0,2,1,0] Output: 1

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1

        while(l <= r):
            middle = (l + r) // 2
            if middle > 0 and arr[middle] < arr[middle - 1]:
                r = middle - 1
            elif middle < len(arr) - 1 and arr[middle] < arr[middle + 1]:
                l = middle + 1
            else:
                return middle

# ------------------------------------------------- 
# 1011. Capacity To Ship Packages Within D Days - weights = [1,2,3,4,5,6,7,8,9,10]  days = 5 / o/p = 18

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity)-> bool :
            curr_day = 1
            total = 0
            for w in weights:
                total += w
                if total > capacity:
                    total = w
                    curr_day += 1
                    if curr_day > days:
                        return False
            return True

        l, r = max(weights), sum(weights) #atleast the ship should be able to carry the highest weight possible
        while(l <= r):            #atmost in the worst case -  the ship should be able to carry all the pacakages in 1 day
            mid = (l + r) // 2
            if feasible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

#---------------------------------------------------------------------------------------------------
# 61. Rotate List 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head

        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length  # Handle k values larger than length - here its 2 again
        if k == 0:
            return head

        new_tail = head
        for i in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        return new_head

# 2. Convert the list [1, 2, 3, 4, 5] into real ListNode objects
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)  # This is the front of your list

# 3. Instantiate the Solution class
sol = Solution()

# 4. Call the method
rotated_head = sol.rotateRight(head, k=2)
#---------------------------------------------------------------------------------------------------
# 141. Linked List Cycle

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def findListCycle(self, head: ListNode):
        slowPointer = head
        fastPointer = head

        if slowPointer != None and fastPointer != None and fastPointer.next != None:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

            if slowPointer == fastPointer:
                return True
        return False

#---------------------------------------------------------------------------------------------------
# 143. Reorder List - Input: head = [1,2,3,4,5] Output: [1,5,2,4,3]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def findListCycle(self, head: ListNode):
        if head is None or head.next is None:
            return
        
        slow_p = head
        fast_p = head.next
        while fast_p and fast_p.next:
            slow_p = slow_p.next            # midpoint
            fast_p = fast_p.next.next

        curr = slow_p.next
        slow_p.next = None                  # cut the link off b/w the first half and the second half
        prev = None                 
        while(curr):                        # reversed second half of the list
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        temp_head, temp_head_2 = head, prev
        while(temp_head_2):
            tmp1, tmp2 = temp_head.next, temp_head_2.next
            temp_head.next = temp_head_2
            temp_head_2.next = tmp1        # we are building 3 nodes in each iteration
            temp_head = tmp1
            temp_head_2 = tmp2

#---------------------------------------------------------------------------------------------------
# 19. Remove Nth Node From End of List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode() 
        dummy.next = head       # starts just before the head node for the purpose of handling edge cases

        fast = dummy
        slow = dummy
        for i in range(n):
            fast = fast.next    # moving the fast pointer to its starting point - very cleaver MODIFIED FLOYYD-WARSHALL

        while(fast.next):
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next  # its removing the undesireable node
        return dummy.next

#---------------------------------------------------------------------------------------------------
# 23. Merge k Sorted Lists

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[List]:
        if not lists or len(lists) == 0:
            return None
        while(len(lists) > 1):
            mergedList = [] #temp var
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedList.append(self.mergeTwoLists(l1, l2))
            lists = mergedList
        return lists[0]


    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while(l1 and l2):
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        return dummy.next

#---------------------------------------------------------------------------------------------------
# 3622. Check Divisibility by Digit Sum and Product

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original_n = n
        sum = 0
        multi = 1
        while n:
            temp = n % 10
            n = n // 10
            sum += temp
            multi *= temp
        return original_n % (sum + multi) == 0 

#---------------------------------------------------------------------------------------------------
# leetcode - 20 - Valid Parentheses

inp = "[({()})]"
class Solution:
    def isValid(self, s: str) -> bool:
        hsh_map = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else: 
                if stack and hsh_map[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True

#---------------------------------------------------------------------------------------------------
# 155. Min Stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.minStack:
            if value <= self.minStack[-1]:
                self.minStack.append(value)
        else:
            self.minStack.append(value)

    def pop(self) -> None:
        if self.stack:
            if self.minStack[-1] == self.stack[-1]:
                self.minStack.pop()
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#---------------------------------------------------------------------------------------------------
# 496. Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {n : i for i, n in enumerate(nums1)}
        ans = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                Idx = nums1Idx[val]
                ans[Idx] = curr
            if curr in nums1Idx:
                stack.append(curr)
        return ans

#---------------------------------------------------------------------------------------------------
# 739. Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonicStack = []
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while monotonicStack and temp > monotonicStack[-1][0]:
                stackTemp, originalIdx = monotonicStack.pop()
                ans[originalIdx] = (i - originalIdx)
            monotonicStack.append([temp, i])
        return ans

#---------------------------------------------------------------------------------------------------
# 3718. Smallest Missing Multiple of K

from typing import List
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        hsh_set = set(nums)
        x = k
        if not nums:
            return None
        while x in hsh_set:
            x += k
        return x

sol = Solution()
print(sol.missingMultiple([42,13,99,13,71,32,64,32,63,44,6,22,8,2,55,88,43,40,71,80,95,32,46,19], 44))

#---------------------------------------------------------------------------------------------------
# 239. Sliding Window Maximum

from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k > len(nums):
            return max(nums)
            
        monoQ = deque()
        ans = []
        l = r = 0

        while r < len(nums):
            while monoQ and nums[monoQ[-1]] < nums[r]:
                monoQ.pop()
            monoQ.append(r)

            if l > monoQ[0]:
                monoQ.popleft()

            if (r + 1) >= k:
                ans.append(nums[monoQ[0]])
                l += 1
            r += 1
        return ans

sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

#---------------------------------------------------------------------------------------------------
# 796. Rotate String

s = "abcde"
goal = "deabc"
for i in range(len(s)):
    s = s[-1:] + s[:-1]
    if s == goal:
        print("True")

#---------------------------------------------------------------------------------------------------
                                # BITWISE FACTORIAL
def bitwise_multiply(a, b):
    result = 0
    while b > 0:
        if b & 1:        # If the lowest bit of b is 1, add 'a' to the result
            result += a
        a <<= 1        # Shift 'a' left (multiply by 2)
        b >>= 1        # Shift 'b' right (divide by 2)
    return result

def bitwise_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    factorial = 1
    for i in range(1, n + 1):
        factorial = bitwise_multiply(factorial, i)
    return factorial

num = 5
print(f"The factorial of {num} is {bitwise_factorial(num)}")  # Output: 120

#---------------------------------------------------------------------------------------------------
# 1004. Max Consecutive Ones III - SLIDING WINDOW O(N) O(1)
 
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_window_len = 0
        num_of_zeroes_so_far = 0

        for r in range(len(nums)):
            curr = nums[r] 
            if curr == 0:
                num_of_zeroes_so_far += 1

            while num_of_zeroes_so_far > k:
                if nums[l] == 0:
                    num_of_zeroes_so_far -= 1
                l += 1  # will run until the "num_of_zeroes_so_far" becomes valid which is <= k

            current_max_window = r - l + 1
            max_window_len = max(max_window_len, current_max_window)
        return max_window_len

#---------------------------------------------------------------------------------------------------
# 643. Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        max_sum = float('-inf')
        temp_sum = 0
        for r in range(len(nums)):
            temp_sum += nums[r]
            temp_sum_count = r - l + 1

            while(temp_sum_count > k):
                temp_sum -= nums[l]
                l += 1
                temp_sum_count = r - l + 1

            if temp_sum_count == k:
                max_sum = max(max_sum, temp_sum)
        return max_sum / k # maximum sum will always return the maximum average

#---------------------------------------------------------------------------------------------------
# 1456. Maximum Number of Vowels in a Substring of Given Length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        current_vowel_count = 0
        for i in range(k):
            if s[i] in vowels:
                current_vowel_count += 1
            
        max_vowels_in_substr = current_vowel_count

        for r in range(k, len(s)):
            if s[r] in vowels:
                current_vowel_count += 1
            if s[r - k] in vowels:
                current_vowel_count -= 1
            max_vowels_in_substr = max(max_vowels_in_substr, current_vowel_count)
        return max_vowels_in_substr

#---------------------------------------------------------------------------------------------------

# LeetCode 340 - is titled "Longest Substring with At Most K Distinct Characters".
# Problem Description : Given a string s and an integer k, 
#                       return the length of the longest substring of s that contains at most k distinct (unique) characters.
# Examples
#     Example 1:
#         Input: s = "eceba", 
#         k = 2
#         Output: 3
#         Explanation: The longest substring with at most 2 distinct characters is "ece", 
#         which has a length of 3.

#     Example 2:
#         Input: s = "aa", 
#         k = 1
#         Output: 2
#         Explanation: The longest substring is "aa" with a length of 2.
# Constraints - 
#     1 ≤ s.length ≤ 5 × 10⁴
#     0 ≤ k ≤ 50
#     s consists of English letters.

from collections import defaultdict
s = "ecebaegdeede"  # 5
k = 2
l = 0
store = defaultdict(int)
max_substring = 0

for r in range(len(s)):
    curr = s[r]
    store[curr] += 1
    while(len(store) > k):
        left_char = s[l]
        store[left_char] -= 1
        if store[left_char] == 0:
            del store[left_char]
        l += 1

    current_substr_len = r - l + 1
    max_substring = max(max_substring, current_substr_len)

print(max_substring)
#---------------------------------------------------------------------------------------------------
# 2091. Removing Minimum and Maximum From Array - with the fewest steps possible

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        # Find indices of min and max elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Ensure i is the smaller index and j is the larger index
        i, j = min(min_idx, max_idx), max(min_idx, max_idx)

        # Three deletion strategies:
        # 1. Delete both from the front (up to index j)
        option1 = j + 1
        # 2. Delete both from the back (back to index i)
        option2 = n - i
        # 3. Delete smaller index from front, larger index from back
        option3 = (i + 1) + (n - j)

        return min(option1, option2, option3)

#---------------------------------------------------------------------------------------------------
# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points - I/p: head = [5,3,1,2,5,1,2] O/p: [1,3]
#           0(n)  0(1)        A critical point in a linked list is defined as either a local maxima or a local minima.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = [-1, -1]
        minDistance = float('inf')
        prev = head
        curr = head.next
        currIndex = 1
        prevCriticalIndex = firstCriticalIndex = 0
        while curr.next :
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val) : 
                if prevCriticalIndex == 0:  # If this is the first critical point found
                    prevCriticalIndex = currIndex
                    firstCriticalIndex = currIndex
                else:
                    # Calculate the minimum distance between critical points
                    minDistance = min(minDistance, currIndex - prevCriticalIndex)
                    prevCriticalIndex = currIndex
            currIndex += 1
            prev = prev.next
            curr = curr.next

        if minDistance != float('inf'):
            maxDistance = prevCriticalIndex - firstCriticalIndex
            result = [minDistance, maxDistance]
        return result

#---------------------------------------------------------------------------------------------------
# 410. Split Array Largest Sum / nums = [7,2,5,10,8], k = 2 , Output: 18
# There are four ways to split nums into two subarrays.The best way is to split it into [7,2,5] and [10,8], 
# where the largest sum among the two subarrays is only 18.
                    # same to same as leetcode - 1011
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(threshold)-> bool:
            count = 1
            total = 0
            for n in nums:
                total += n
                if total > threshold:
                    total = n
                    count += 1
                    if count > k:
                        return False
            return True

        l, r = max(nums), sum(nums)
        while(l <= r):
            mid = (l + r) // 2
            if feasible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

#---------------------------------------------------------------------------------------------------
# 875. Koko Eating Bananas  - Input: piles = [30,11,23,4,20], h = 5 Output: 30

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed)-> bool :
            return sum(((pile - 1) // speed) + 1 for pile in piles) <= h #(e.g pile = 7, speed + 2, ((7 - 1) // 2) + 1 = 3 hours

        l, r = 1, max(piles)    # at minimum speed koko has to eat is 1 bananna/h at max its restricted to only one pile, 
        while(l <= r):          # -highest that can be is the pile with max bananas
            mid = (l + r) // 2
            if feasible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

#---------------------------------------------------------------------------------------------------
# 148. Sort List - Input: head = [4,2,1,3] Output: [1,2,3,4] time-col => O(NLOGN) space col => O(LOG N)

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slowP = head
        fastP = head.next
        while(fastP and fastP.next):
            slowP = slowP.next
            fastP = fastP.next.next
        mid = slowP.next
        slowP.next = None

        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while(l1 and l2):
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next

#---------------------------------------------------------------------------------------------------
# 88. Merge Sorted Array - nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 / Tcol - O(m + n) Scol - O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

#---------------------------------------------------------------------------------------------------
# leetcode - 27 / remove element / nums = [3, 2, 2, 4, 9, 7, 2, 2], val = 2, o/p = [3, 4, 9, 7, _, _, _, _] ? k = 4
                                                                                            #k
nums = [0,1,2,2,3,0,4,2]
val = 2

original_length = k = len(nums)
for i in range(len(nums) - 1, -1, -1):
    if nums[i] == val:
        print(f"popped at pos : {i} el ", nums.pop(i))
        k -= 1

del_el_count = original_length - k
print(nums.extend([0] * del_el_count))

print(nums, k)
#---------------------------------------------------------------------------------------------------
# 678. Valid Parenthesis String | s containing -> '(', ')' and '*', '*' could be ')' or '(' or an empty string "".
#                                              ex - Input: s = "(*))" Output: true
class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return False
        openParenthesisStack = []
        starStack = []
        for i in range(len(s)):
            if s[i] == "(":
                openParenthesisStack.append(i)
            elif s[i] == "*":
                starStack.append(i)
            else:
                if openParenthesisStack:
                    openParenthesisStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False

        while openParenthesisStack and starStack:
            if openParenthesisStack[-1] > starStack[-1]:
                return False
            openParenthesisStack.pop()
            starStack.pop()

        return len(openParenthesisStack) == 0

#---------------------------------------------------------------------------------------------------
# PostFix Expression Evaluation
def evaluate_postfix_space(expression: str) -> float:
    stack = []

    # Splitting by whitespace handles multi-digit numbers perfectly
    for token in expression.split():        # we dont have to pass anything in split method, that indicates to spaces  
        if token in ["+", "-", "*", "/"]:
            b = stack.pop()
            a = stack.pop()
            
            if token == "+": stack.append(a + b)
            elif token == "-": stack.append(a - b)
            elif token == "*": stack.append(a * b)
            elif token == "/": stack.append(a / b)
        else:
            # Converts multi-digit string tokens (like "12") to actual floats
            stack.append(float(token))

    return stack[-1]

# --- Test Cases ---
print(evaluate_postfix_space("12 3 /"))       # Output: 4.0
print(evaluate_postfix_space("100   25 / 5 +")) # Output: 9.0 (Handles extra spaces perfectly!)
#---------------------------------------------------------------------------------------------------
# 3870. Count Commas in Range - Return the total number of commas used when writing all integers from [1, n]
                    #For 1 Millon -> 999001
# 3871. Count Commas in Range II -> Same Code

class Solution:
    def countCommas(self, n: int) -> int:
        if not n:
            return 0
        if len(str(abs(n))) < 4:
            return 0
        count_of_commas = 0
        factor = 1000
        while(n >= factor):
            count_of_commas += (n - factor + 1)
            factor *= 1000
        return count_of_commas

#---------------------------------------------------------------------------------------------------
# 1006. Clumsy Factorial - For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.

import itertools
class Solution:
    def clumsy(self, n: int) -> int:
        if not n:
            return None
        list_of_opr = ['*', '/', '+', '-']
        list_of_opr_cycle = itertools.cycle(list_of_opr)
        stack = [n]
        for i in range(n-1, 0, -1):
            op = next(list_of_opr_cycle)
            if op == "*":
                stack.append(stack.pop() * i)
            elif op == "/":
                stack.append(int(stack.pop() / i))
            elif op == "+":
                stack.append(i)
            elif op == "-":
                stack.append(-i)
        return sum(stack)

#---------------------------------------------------------------------------------------------------
# 151. Reverse Words in a String

s = "hello world from the above    of the world  "
arr1 = s.split()

rev_str = " ".join(arr1[::-1])

print(arr1)
print(rev_str)
#---------------------------------------------------------------------------------------------------
# 46. Permutations

def permutations(current_array):
    # We have selected enough elements
    if len(current_array) == len(array):
        print(current_array)
        return 
    
    # Try every element as the NEXT element
    for curr in array:
        # Don't use an element twice
        if curr not in current_array:
            current_array.append(curr)  # CHOOSE
            permutations(current_array) # GO DEEPER
            current_array.pop()         # UNDO

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5] # For Lists
    permutations([])

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
    string = "abcde"        # For Strings
    print(permutation_string([], []))
#---------------------------------------------------------------------------------------------------
# 39. Combination Sum - Input: candidates = [2,3,6,7], target = 7 - Output: [[2,2,3],[7]] Tcol - 2^t x k  Scol - Unpredictable

class Solution:
    def subarray_sum_equals_k(self, index, candidates, target, current_subarray, output, current_sum):
        if current_sum == target:
            output.append(current_subarray.copy())
            return 
        if current_sum > target or index == len(candidates):
            return

        current_subarray.append(candidates[index])
        current_sum += candidates[index]
        self.subarray_sum_equals_k(index, candidates, target, current_subarray, output, current_sum)    # All Possible cominations including same elements
        
        current_sum -= current_subarray.pop()
        self.subarray_sum_equals_k(index + 1, candidates, target, current_subarray, output, current_sum)    # Possile combination excluding the already done elemnts
        return output

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or not target:
            return []
        return self.subarray_sum_equals_k(0, candidates, target, [], [], 0)

#---------------------------------------------------------------------------------------------------
# 58. Length of Last Word - Input: s = "   fly me   to   the moon  "  Output: 4

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trimmed_up = s.strip()
        if not trimmed_up:
            return 0
        length = 0
        for char in range(len(trimmed_up) - 1, -1, -1):
            if trimmed_up[char] == ' ':
                break
            length += 1
        return length

#---------------------------------------------------------------------------------------------------
# 40. Combination Sum II

class Solution:
    def subarray_sum_equals_k(self, index, candidates, target, current_subarray, output):
        if target == 0:
            output.append(current_subarray.copy())
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue        # Skip duplicate choices at the same level
            if candidates[i] > target:
                break           # Since array is sorted

            current_subarray.append(candidates[i])
            self.subarray_sum_equals_k(i + 1, candidates, target - candidates[i], current_subarray, output)
            current_subarray.pop()
        return output

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or not target:
            return []
        candidates.sort()
        return self.subarray_sum_equals_k(0, candidates, target, [], [])

#---------------------------------------------------------------------------------------------------
# LeetCode - 78 Subsets I- Pinting all the subsets of a given Array /List  - Timecol -> O((2^n) x n)

def print_subsequences(index, array:List, current_subseq_arr):
    if index >= len(array):
        # print(current_subseq_arr)
        return
    current_subseq_arr.append(array[index])
    print_subsequences(index + 1, array, current_subseq_arr)    # Take or pick the particular index into the subsequence

    current_subseq_arr.pop() #remove the current element(backtrack)
    # Not Pick or not take condition, this element is not added to your subsequence
    print_subsequences(index + 1, array, current_subseq_arr)

if __name__ == "__main__":
    arr1 = [3, 1, 2]
    print_subsequences(0, arr1, [])

#---------------------------------------------------------------------------------------------------
# 90. Subsets II - Input: nums = [1,2,2] Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
                            # May Contain Duplicate values in a subset, but not duplicates subsets
def subsets_II(index, arr, current_subarray, output):
    output.append(current_subarray.copy())

    for i in range(index, len(arr)):
        if i != index and arr[i] == arr[i-1]:
            continue

        current_subarray.append(arr[i])
        subsets_II(i + 1, arr, current_subarray, output)

        current_subarray.pop()
    return output

if __name__ == "__main__":
    arr = [3, 1, 2, 2]
    arr.sort()
    # print(subsets_II(0, arr, [], []))

#---------------------------------------------------------------------------------------------------
# 47. Permutations II - Input: nums = [1,1,2] Output: [[1,1,2], [1,2,1], [2,1,1]]
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

class Solution:
    def all_possible_with_duplicates(self, nums, current_permutation, output, used):
        if len(current_permutation) == len(nums):
            output.append(current_permutation.copy())
            return
        
        for i in range(len(nums)):
            if used[i]:     # Have we already used this index?
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:    # Skip duplicate choices at the same level
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

#---------------------------------------------------------------------------------------------------
# LeetCode - 60. K-th Permutation(Permutation Sequence) Tcol- O(n! . n), Scol- 0(K.n)

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

#---------------------------------------------------------------------------------------------------
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

#---------------------------------------------------------------------------------------------------
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

#---------------------------------------------------------------------------------------------------
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

#---------------------------------------------------------------------------------------------------
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

#---------------------------------------------------------------------------------------------------
# 3498. Reverse Degree of a String

import string
class Solution:
    def reverseDegree(self, s: str) -> int:
        if not s:
            return 0
        char_map = {char: i+1 for i,char in enumerate(reversed(string.ascii_lowercase))}
        sum = 0
        product = 1
        for i in range(len(s)):
            product = (i + 1) * char_map[s[i]]
            sum += product
        return sum

#---------------------------------------------------------------------------------------------------
# 69. Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        low = 0
        mid = high = x
        while low <= high:
            mid = (low + high) // 2
            mid_sqr = mid * mid
            if mid_sqr == x:
                return mid
            elif mid_sqr < x:
                ans = mid        # mid could be the truncated answer, save it
                low = mid + 1    # look in the upper half
            else:
                high = mid -1    # too high, look in the lower half

        return int(ans)

#---------------------------------------------------------------------------------------------------
# 4. Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        temp = []
        left = right = 0
        nums1high = len(nums1) - 1
        nums2high = len(nums2) - 1
        while left <= nums1high and right <= nums2high:
            if nums1[left] <= nums2[right]:
                temp.append(nums1[left])
                left += 1
            else:
                temp.append(nums2[right])
                right += 1
        while left <= nums1high:
            temp.append(nums1[left])
            left += 1
        while right <= nums2high:
            temp.append(nums2[right])
            right += 1
        mid = (0 + (len(temp) - 1)) // 2
        if len(temp) % 2 == 0:
            return ((temp[mid] + temp[mid + 1]) / 2)
        else:
            return (float(temp[mid]))

#---------------------------------------------------------------------------------------------------
# 1658. Minimum Operations to Reduce X to Zero - Using Sliding Window O(N), 0(1)

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        if not nums or not x:
            return -1
        target = sum(nums) - x

        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        
        left = 0
        max_len = -1
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > target:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
        if max_len == -1:
            return -1
        else:
            return len(nums) - max_len 
            
#---------------------------------------------------------------------------------------------------
# 3550. Smallest Index With Digit Sum Equal to Index
 
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        for i, num in enumerate(nums):
            numsum = 0
            while(num > 0):
                temp = num % 10
                numsum += temp
                num = num // 10
            if i == numsum:
                return i
        return -1

#---------------------------------------------------------------------------------------------------
# 6. Zigzag Conversion | Input: s = "PAYPALISHIRING", numRows = 4 | Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N              |    /|    /|    /|
# A   L S  I G              |  ^  |  ^  |  ^  |
# Y A   H R                 |/    |/    |/    |
# P     I                   |     |     |     

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 :
            return s
        rows = [""] * numRows
        current_row = 0
        going_down = False  # Direction flag

        for char in s:
            rows[current_row] += char   # Add character to the current row

            if current_row == 0 or current_row == numRows - 1:  # Change direction when hitting the top or bottom row
                going_down = not going_down     # Reverse direction
            
            current_row += 1 if going_down else -1  # Move to the next row based on direction
        return "".join(rows)    # Join all rows together to get the final transformed string

#---------------------------------------------------------------------------------------------------
# 1807. Evaluate the Bracket Pairs of a String - Input: s = "(name)is(age)yearsold", 
# knowledge = [["name","bob"],["age","two"]] Output: "bobistwoyearsold"

s = "(name)is(age)yearsold"
knowledge = [["a","b"]]
key_val = dict(knowledge)
print(key_val)
replaceables = []
output = ""
char = 0

while char != len(s):   # General Loop
    replacement_char = ""
    if s[char] == "(":  #Replacabloe chars
        char += 1
        while(s[char] != ")"):
            replacement_char += s[char] 
            char += 1
        char += 1
    if replacement_char:
        found_it = False
        if replacement_char in key_val:
                found_it = True
                output += key_val[replacement_char]
        if not found_it:
            output += "?"
    else:
        output += s[char]
        char +=1

print(output)

#---------------------------------------------------------------------------------------------------






#---------------------------------------------------------------------------------------------------






#---------------------------------------------------------------------------------------------------







#---------------------------------------------------------------------------------------------------








#---------------------------------------------------------------------------------------------------







#---------------------------------------------------------------------------------------------------







#---------------------------------------------------------------------------------------------------
