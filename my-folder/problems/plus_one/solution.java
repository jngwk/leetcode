class Solution {
    public int[] plusOne(int[] digits) {
        for(int i=digits.length - 1; i>=0; i--){
            digits[i] ++;
            if(digits[i] == 10){
                digits[i] = 0;
            }else{
                break;
            }
        }

        if(digits[0] == 0){
            int[] newDigits = new int[digits.length + 1];
            newDigits[0] = 1;
            for(int i=1; i<newDigits.length; i++){
                newDigits[i] = digits[i-1];
            }
            return newDigits;
        }
        else{
            return digits;
        }
    }
}