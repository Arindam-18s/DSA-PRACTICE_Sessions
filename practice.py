chars = ["a","a","b","b","c","c","c"]

print(chars)

maps = {}
opl = []

for char in chars:
    if char not in maps:
        maps[char] = 1
    elif char in maps and char == char:
        maps[char] += 1

for char, count in maps.items():
    if count == 1:
        opl.append(char)
    else:
        opl.append(char)
        opl.append(count)

chars[:] = opl

print(maps)
print(chars)
print(opl)


