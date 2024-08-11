class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # if target is in nums:
        #     return nums.index(target)

        for i, val in enumerate(nums):
            if val >= target:
                return i
        return len(nums)


