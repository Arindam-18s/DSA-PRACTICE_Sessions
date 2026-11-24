nums = [-1, 2, 3, 4 , -3, 1, 4, -3]             # Time - O(2N), Space - O(N)
N = len(nums)
pos = []
neg = []

for i in range(N):
    if nums[i] > 0:
        pos.append(nums[i])
    else:
        neg.append(nums[i])

if len(pos) > len(neg):
    for i in range(len(neg)):
        nums[2 * i] = pos[i]
        nums[2 * i + 1] = neg[i]

    remaining_pos_idx = len(neg) * 2        # Remainning Elements in the positive elements array
    for j in range(len(neg), len(pos)):
        nums[remaining_pos_idx] = pos[j]
        remaining_pos_idx += 1
else:
    for i in range(len(pos)):
        nums[2 * i] = pos[i]
        nums[2 * i + 1] = neg[i]

    remaining_pos_idx = len(pos) * 2        # Remainning Elements in the negative elements array
    for j in range(len(pos), len(neg)):
        nums[remaining_pos_idx] = neg[j]
        remaining_pos_idx += 1

print(nums)
