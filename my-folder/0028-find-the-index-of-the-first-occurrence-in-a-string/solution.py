class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
          print("not in haystack")
          return -1
        
        for i in range(len(haystack) - len(needle) + 1):
          if needle == haystack[i: i + len(needle)]:
            return i
            
        return -1
