# s = "))())("

# map = {"left_parenthesis": 0, "right_parenthesis": 0}
# i = 0
# while i < len(s):
#     if s[i] == "(":
#         map["left_parenthesis"] += 1
#         print(f"left ( at pos - {i}")
#         i += 1
#     elif s[i] == ")":
#         print(f"right ) at pos - {i}")
#         if map["left_parenthesis"] > 0:
#             if s[i + 1]:
#                 if s[i + 1] == ")":
#                     map["left_parenthesis"] -= 1
#                     i += 1
#             else:
#                 map["right_parenthesis"] += 1
#         else:
#             map["right_parenthesis"] += 1
#         i += 1
# print("( : ", map["left_parenthesis"], ",  ) : ", map["right_parenthesis"])


s = "))())("

i = 0
j = 1
minimum = 0
while j < len(s):
    if s[i] == "(":
        if s[j] == ")":
            if s[j + 1] == ")":
                i += 3
                j += 3
        elif s[j] == "(":
            minimum += 1
        
    elif s[i] == "("