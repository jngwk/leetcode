class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        numSet = set()
        for i in range(len(nums)):
            if nums[i] in numSet:
                return True
            numSet.add(nums[i])

        return False
