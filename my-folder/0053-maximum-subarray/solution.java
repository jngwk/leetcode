class Solution {
    public int maxSubArray(int[] nums) {
        int sum = 0;
        int maxSum = nums[0];
        for(int num: nums){
            sum += num;
            maxSum = sum > maxSum ? sum : maxSum;

            // 음수이면 최대일리가 없기 때문에 0으로 초기화
            if(sum < 0){
                sum = 0;
            }
        }
        return maxSum;
    }
}
