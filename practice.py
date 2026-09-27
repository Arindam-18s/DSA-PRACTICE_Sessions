s = "(ed(et(oc))el)"
stack = []
ans = ""

for char in s:
    if char == "(":
        stack.append(ans)
        ans = ""
    elif char == ")":
        ans = ans[::-1]
        ans = stack.pop() + ans
    else:
        ans += char

print(ans)
    