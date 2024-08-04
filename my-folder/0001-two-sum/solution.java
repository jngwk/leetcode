class Solution {
    public int[] twoSum(int[] nums, int target) {
        if(nums.length == 2){
            return new int[] {0,1};
        }
        Map<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            int complement = target - nums[i];
            if(!map.containsKey(complement)){
                map.put(nums[i], i);
            }
            else {
                return new int[] {map.get(complement), i};
            }
        }

        return null;
    }
}
