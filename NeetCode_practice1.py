# --- Variables --- are dynamicly typed (we dont have to declare that, TYPES ARE DETERMINED AT RUN TIME, HERE n has no type for Now)
n = 5
# print("n = ", n)

n = "abc"
# print("n = ", n)

# --- Multiple assignments ---
n, m = 0, "abc"

n, m, z = 0.125, "abc", False

# print("n = ", n, m, z)  
# print("m = ", m)
# print("z = ", z)

# --- Increment ---
n = n + 1   #good
n += 1      #good
# n++         #bad

# --- None is null --- (Absense of value)
n = None
# print("n = ", n)

# --- If statements --- doesn't need parentheses or curly braces
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

# Parentheses needed for multi-line conditions.
# and = &&
# or = ||
n, m = 1, 2
if((n > 2 and n != m) or n == m):
    n +=1

# --- While --- loops are similar
n = 0
while(n < 5):
    # print(n)
    n += 1

# --- for --- looping from i = 0 to i = 4
for i in range(5):   # i will be incremented implecitely, we dont have to define i += num to increment 
    # print(i)
    a = i

# for looping from i = 2 to i = 5
for i in range(2, 6):   # i will be incremented implecitely, we dont have to define i += num to increment 
    # print(i)
    a = i

# for looping from i = 5 to i = 2 (Decrementing)
for i in range(5, 1, -1):   # -1 for the sake of decrementing the loop val
    # print(i)
    a = i

# --- Division --- is decimal By default
# print(5 / 2)

# Double slash Rounds Down
# print(5 // 2)

# CAREFUL : most languages round towards 0 by default, so negative numbers will round down.
# print(-3 // 2)  # it gives answer: -2

# A workaround for rounding towards zero is to use decimal division and then covert to integer.
# print(int(-3 / 2))

# --- Modding --- is similar to most languages
# print(10 % 3)

# Modding is similar to most languages -  Except for negative values
# print(-10 % 3)

# TO-be consistant with how other languages implement modulo
import math
# print(math.fmod(-10 , 3))

# More Math Helpers
# print(math.floor(3 / 2))
# print(math.ceil(7 / 2))
# print(math.sqrt(9))
# print(math.pow(2, 3))

# --- Max / Min --  Int
float("inf")
float("-inf")

# --- Python numbers are infinite --- so they never overflow
# print(math.pow(2, 200))

# But still less than infinity
# print(math.pow(2, 200) < float("inf")) # it gives a o/p - True

# Arrays(called lists in python) -- LISTS --
myList = [1, 2, 3]
# print(myList)
                                    #Lists are not hashable, so they can't be Keys For Hahsets
# Can be used as a STACK - Cause Arrays are dynamic in python by default
myList.append(4)
myList.append(5)
# print(myList)

myList.pop()
# print(myList)

myList.insert(0, 69)   # can also use the insert function in it - [69, 1, 2, 3, 4]
# print(myList)

# print(myList[3])       # index an array - we can read and reassign the value by using indexing method also
myList[2] = 20
# print(myList)

# number to list using slicing
num = 12345
digit_list = [int(d) for d in str(num)]

# initialize myList of size n with default value of 1
n = 5
myList = [1] * n
# print(myList)
# print(len(myList))

# CAREFUL: -1 is not out of bounds, its the last value
myList = [1, 2, 3]
# print(myList[-1])  # is gives the answer - 3

# Indexing -2 to read the second to last value etc.
# print(myList[-2])

# Sublists (aka slicing an myList)
myList = [1, 2, 3, 4]
# print(myList[1 : 3])   #this gives the answer [2, 3]

# Unpacking 
a, b, c = [1, 2, 3]     # we can take every single value of a List and assign 'em to variables
# print(a, b, c)

# Be CAREFUL though
# a, b = [1, 2, 3]    # <-- the number of items on the left hand side should be equal to the number of array elements on the right hand side
 
# Loop Through Lists(Arrays) -->
nums = [1, 2, 3]
# Using index
for i in range(len(nums)):
    # print(nums[i])
        a = i

# Without index
for n in nums:
    # print(n)
        a = i

# With index and value
for i,n in enumerate(nums):
    #  print(i, " : ", n)     #printing index and values both
    a = i

# Loop through Multiple arrays simulteneously - with Unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):    # helper func called zip - which combines these arrays as pairs
    # print(n1, n2)
    a = i

# Reverse
nums1 = [1, 3, 5]
nums1.reverse()
# print(nums1)

# Sorting 
myList = [4, 2, 8, 6, 1]
myList.sort()      # ascending by default
myList.sort(reverse=True)  # for decending order
# print(myList)

myList = ["alice", "jane", "cera", "bob"]  # Sorting list of strings
myList.sort() # ascending by default

myList.sort(key=lambda x: len(x))  # Custom sort - by length of string
# print(myList)

# List Comorehension
myList = [i for i in range(5)]
# print(myList)

# --- 2-D lists --- through list comprehension
myList = [[2] * 4 for i in range(4)]
# print(myList)

# --- Strings --- (strings are similar to arrays)
s = "abc "
# print(s)
# print(s[0:2]) # can also perform slicing on strings

# s[0] = "A" # <-- But Strings are IMMUTABLE(i.e. we cannot modify the position already occupied by some character, after we've defined it)
s += "is Free" #we can however update it in a way - which create a new String
# print(s)

# print(int("123") + int("123"))  # Valid numeric Strings can be converted
# print(str(123) + str(123))      # And numbers can be converted to strings

# In Rare Cases u might need the -- ASCII val -- of a charactor
# print(ord("a"))
# print(ord("b"))

# Combine a List of strings - (with an empty string delimitor)
Strings = ["Life-" "liberty-" "And the persuit of happiness"]
# print("".join(Strings))

# --- Queue --- ( in python queue's are Double ended by default)
from collections import deque
queue = deque() #queue gets appended from the right side -> deque([1, 3, 4])
queue.append(1)
queue.append(3)
queue.append(4)
# print(queue)

queue.popleft() #deleting from the left

queue.appendleft(1)  #appending from the left side as its a double ended Queue

queue.pop()     #deleting from the right side as its a double ended Queue

# --- Hashsets ---
mySet = set()   #it cannot have duplicate values

mySet.add(1)
mySet.add(2)
# print(mySet)
# print(len(mySet))

# print(1 in mySet)   #we can search a val in hashset using the - "in" - function  | it gievs either True/False
mySet.remove(1)     #we can remove values
# print(mySet)

# list to set (initializing hashset with a bunch of values)
# print(set([1, 2, 3]))

# set Comprehension
mySet = { i for i in range(5) }
# print(mySet)

# --- HashMaps(aka dict) ---    #Can't have duplicate Keys inside of the hashmap
myMap = {}
myMap["Alice"] = 12 
myMap["Bob"] = 31 
myMap = { "Poltu" : 69, "Biltu" : 43 }   #Same as manually inserting values one by one 
# print(myMap)    # {'Alice': 12, 'Bob': 31}
# print(len(myMap)) # print the number of Keys that are in the hashMap

myMap["Bob"] = 21   # can change the values for keys
# print(myMap["Bob"])        #  21

# print("Alice" in myMap) # searching for a key in hashmap  -> True
myMap.pop("Bob")    #remove key-val in HashMap

#Dict Compreshension Val inserting in HashMap
myMap = { i: 2*i for i in range(3)}    # {0: 0, 1: 2, 2: 4}
# print(myMap)

#Looping Through HashMaps
myMap = { "Poltu" : 69, "Biltu" : 43 }
for key in myMap:
    #  print(key, myMap[key])
    a = i
     
for val in myMap.values():
    #  print(val)
    a = i

for key,val in myMap.items():
    #  print(key, val)
    a = i

# --- Tuples --- These are like arrays but immutable
tup = (1, 2, 3)
# print(tup)
# print(tup[0])   #we can index them
# tup[1] = 2  #can't modify tuples

# Tuples Can be used as Key for Hash map/set   |   #Lists are not hashable, so they can't be Keys For Hahsets
myMap = { (1,2) : 3 }
# print(myMap[(1,2)])  #3

mySet = set()
mySet.add((1, 2))
# print((1,2) in mySet)   #searching - it gives True

# --- Heaps --- (Under the Hood they are actually arrays)
import heapq

minHeap = []        #By default heaps in python are meanHeaps
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 6)
heapq.heappush(minHeap, 1)
# print(minHeap)      # The min value of the Heap wil always be at index 0 - [1, 6, 3]

# while len(minHeap):     #looping through heap
    #  print(heapq.heappop(minHeap))  #pop function

# ---- Functions in Py -----
def myFunc(n, m):
     return n+m

# print(myFunc(2,3))

# --- Nested Functions --- these have access to outer variables
def outer(a, b):        #Nested Functions - can modify objects but not reassign, unless using non-local keyword
     c = "c"

     def inner():
          return a + b + c
     return inner()

print(outer("a", "b"))  # abc

# --- Class ---
class myClas:
     #Constructor
     def __init__(self, nums):      # self is passed to every method of a class
         #Create member Variables
         self.nums = nums
         self.size = len(nums)

         #creating a method for this class - self keyword required as param(give us access to our member variable)
         def getLength(self):
            return self.size

         def DoubleLength(self):
            return 2 * self.getLength()
              