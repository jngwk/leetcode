class Solution {
    public int maxArea(int[] height) {
        int lp = 0;
        int rp = height.length - 1;
        int maxArea = 0;

        while(lp < rp){
            int h = height[lp] < height[rp] ? height[lp] : height[rp];
            int l = rp - lp;
            int currentArea = l*h;
            maxArea = currentArea > maxArea ? currentArea : maxArea;

            // if(height[lp] > height[rp]){
            //     rp --;
            // }else{
            //     lp ++;
            // }

            while(height[lp] <= h && lp < rp) lp ++;
            while(height[rp] <= h && lp < rp) rp --;
        }

        return maxArea;
    }
}
