class Solution:
    def isValid(self, s: str) -> bool:
      if len(s) % 2 != 0:
        print("odd length")
        return False
      test = {')':'(', '}':'{', ']':'['}
      open = []
      for i in range(len(s)):
        if s[i] in test:
          # print(s[i])
          # print(test[s[i]])
          if len(open) <= 0 or open.pop() != test[s[i]]:
            print("not valid")
            return False
        else:
          open.append(s[i])
      
      if len(open) == 0:
        return True
      else:
        return False

