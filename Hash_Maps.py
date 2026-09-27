# HashMAPS

city_map = {}        # <-initialization

city_maps = dict()   # <-initialization
#-------------
# Appending
cities = ["toronto", "vancouver", "monterial"]
# city_map["cananda"] = []        #<-first have to initialize the key
# city_map["cananda"] += cities

# print(city_map)
#-------------
#to avoid manually declairing every single dict, we use this sintax
from collections import defaultdict
city_map = defaultdict(list)
city_map["cananda"] += cities

print(city_map)

print(city_map.values())    # -> dict_values([['toronto', 'vancouver', 'monterial']])

print(city_map.keys())      # -> dict_keys(['cananda'])

print(city_map.items())     # -> dict_items([('cananda', ['toronto', 'vancouver', 'monterial'])])

#----------------------------------------------------------------------------------------------
# HashSets  - O(n)
# 217. Contains Duplicate - we have to use hashsets in these situations  -  Input: nums = [1,2,3,1]  Output: true
class Solution(object):
    def containsDuplicate(self, nums):
        h = set()
        for num in nums:
            if num in h:
                return True
            else:
                h.add(num)

        return False

#----------------------------------------------------------------------------------------------
# 49. Group Anagrams
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        
        for value in anagram_map.values():
            result.append(value)
        
        return result
#----------------------------------------------------------------------------------------------
# Two SUM
seen = {}  # will store {value: index}

for i, num in enumerate(nums):
    complement = target - num  # For each number, check if its "complement" (the number needed to reach the target) 
    if complement in seen:     # has already been seen.If yes, you found your pair. If no, 
        print [seen[complement], i] # remember this number's value and index for future checks.
    seen[num] = i
#----------------------------------------------------------------------------------------------
import random
from collections import Counter

obj_list = ["A", "B", "C", "D", "E"]

random_list = random.choices(obj_list, k=100)
counter = Counter(random_list)

print(random_list)
print(counter.most_common()[:2])

# for _ in range(100):
#     recieved_obj = random.choice(obj_list)
#     counter[recieved_obj] += 1

# print(counter.total())