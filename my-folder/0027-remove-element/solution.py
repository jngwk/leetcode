class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[p] = nums[i]
                p += 1 
        
        return p 
