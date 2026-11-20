nums = [1]
N = len(nums)
max_el = float('-inf')
for i in range(N):
    if nums[i] > max_el:
        max_el = nums[i]

hash_arr = [0] * (max_el + 1)

for k in range(N):
    hash_arr[nums[k]] += 1

for j in range(max_el + 1):
    if hash_arr[j] == 1:
        print(j)
        break


