class Solution {
    public int searchInsert(int[] nums, int target) {
        int p1 = 0;
        int p2 = nums.length-1;

        while(p1 <= p2){
            int center = (p2 + p1) / 2;
            if(target < nums[center]){
                p2 = center - 1;
            }else if(target > nums[center]){
                p1 = center + 1;
            }else{
                return center;
            }
        }

        return p1;
    }
}
