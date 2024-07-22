class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length == 1){
            return 1;
        }
        int p = 0;
        for(int i=1; i<nums.length; i++){
            if(nums[i] != nums[p]){
                nums[++p] = nums[i];
            }
        }
        return p+1;
    }
}