s = "00000000"
k = 3
chunk_sum = 0

while len(s) > k:
    temp_s = ""
    for i in range(0, len(s), k):
        chunk_sum = 0
        j = i
        while j < i + k and j < len(s):
            chunk_sum += int(s[j])
            j += 1
        print(chunk_sum)
        temp_s += str(chunk_sum)
    s = temp_s

print(s)