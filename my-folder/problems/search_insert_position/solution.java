class Solution {
    public int searchInsert(int[] nums, int target) {
        int lp = 0;
        int rp = nums.length - 1;

        while(lp <= rp){
            int k = (rp + lp) / 2;
            if(target < nums[k]){
                rp = k - 1;
            }
            else if(target > nums[k]){
                lp = k + 1;
            }
            else{
                return k;
            }
        }

        return lp;
        // if(target < nums[lp]){
        //     if(lp == 0){
        //         return lp;
        //     }
        //     return lp - 1;
        // }
        // else{
        //     return lp + 1;
        // }
    }
}