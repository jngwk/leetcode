class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = -inf
        start =  0
        end = len(height) - 1
        
        while start < end:
            area = min(height[start], height[end]) * (end - start)
            maxArea = max(area, maxArea)
                   
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return maxArea

