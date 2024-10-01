class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        isChanged = False
        for i in range(len(nums) - 1, 0, -1):
          if nums[i] > nums [i-1]:
            sorted_arr = sorted(nums[i:])
            if sorted_arr[0] < nums[i] and sorted_arr[0] > nums[i-1]:
              print("in")
              temp = nums[i-1]
              nums[i-1] = sorted_arr[0]
              sorted_arr[0] = temp
              nums[i:] = sorted_arr
              isChanged = True
              break
            
            if nums[i-1] >= sorted_arr[0] and nums[i-1] < sorted_arr[-1]:
              print("in another")
              for j, num in enumerate(sorted_arr):
                if num > nums[i-1]:
                  temp = nums[i-1]
                  nums[i-1] = num
                  sorted_arr[j] = temp
                  break
              nums[i:] = sorted_arr
              isChanged = True
              break
            
            temp = nums[i]
            nums[i] = nums[i-1]
            nums[i-1] = temp
            nums[i:] = sorted(nums[i:])
            isChanged = True
            break
        if not isChanged:
          nums.sort()
