class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def numberToBase(n, b):
          if n == 0:
              return [0]
          digits = []
          while n:
              digits.append(int(n % b))
              n //= b
          return digits[::-1]

        def isPalindromic(arr):
          return arr[::-1] == arr
          # pt = len(arr) - 1
          # for i in range(len(arr) // 2):
          #   if(arr[i] != arr[pt]):
          #     return False
          #   pt -= 1
          # return True

        for i in range(n-2, 1, -1):
          arr = numberToBase(n, i)
          if not isPalindromic(arr):
            return False
        return True

