haystack = "mississippi"
needle = "issip"
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or not needle or len(needle) > len(haystack):
            return -1
        i = j = 0
        while i < len(haystack):
            if  haystack[i] == needle[j]:
                print("Main Stack : ", haystack[i], "+  Substr : ", needle[j])
                i += 1
                j += 1
                if j == len(needle):
                    return i - j    # Mathematical Formula to find the first occurance of the string
            else:
                i = i - j + 1       # Rollback 'i' to the next starting character after where this match began
                j = 0
        return -1
