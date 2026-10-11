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





# 388. Longest Absolute File Path






# input_str = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

# # 1. Split the string into a list of lines
# lines = input_str.split("\n")

# # 2. Reverse the list order (leaves the words themselves untouched)
# reversed_lines = lines[::-1]

# # 3. Join them back together with newlines
# result = "\n".join(reversed_lines)
# for char in result:
#     print(char)

# occ = result.find("file")

# print(occ)
