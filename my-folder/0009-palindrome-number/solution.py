class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversed = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed = reversed * 10 + digit
            temp //= 10
        
        return x == reversed
