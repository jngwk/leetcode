class Solution {
    public int removeElement(int[] nums, int val) {
        if(nums.length == 0){
            return 0;
        }
        int index = 0;
        for(int i=0; i<nums.length; i++){
            // if nums[i] is not val, insert into index
            if(nums[i] != val){
                nums[index ++] = nums[i];
            }
            // else if nums[i] is val skip
        }

        return index;
    }
}
