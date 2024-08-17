class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = -inf
        maxSum = -inf
        
        for i, n in enumerate(nums):
            sum = max(n, sum + n)
            maxSum = max(sum, maxSum)
        
        return maxSum

