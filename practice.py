import sys
sys.setrecursionlimit(2000000)

def rec(i, str1):
    if i >= len(str1):
        return str1
    if str1[i] == 'a':
        str1 = str1[:i] + str1[i + 1:]
        return rec(i , str1)
    return rec(i + 1, str1)

def skipAskedWord(str_to_remove : str, str2 : str):
    pattern_to_find = f",{str_to_remove},"
    current_pattern_idx = str2.find(pattern_to_find)

    if current_pattern_idx == -1:      # Base Case: If the pattern isn't found anywhere, we are done!
        return str2
    
    str2 = str2[:current_pattern_idx] + str2[current_pattern_idx + len(pattern_to_find) - 1 :]
    return skipAskedWord(str_to_remove, str2)

str1 = "hjihaaaaa"
str2 = "Banana,Guava,Mango,Apple,App,App,Pinnaple,Apple,Jackfruit,AppStore,Appoxy,App"
# print(rec(0, str1))
print(skipAskedWord('App',str2))
