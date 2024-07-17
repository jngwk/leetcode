class Solution {
    public int romanToInt(String s) {
        char[] charArr = s.toCharArray();
        int result = 0;
        int n = charArr.length;
        int x;
        for (int i = n - 1; i >= 0; i--) {
            switch (charArr[i]) {
                case 'I':
                    x = 1;
                    // subtraction cases
                    if (i + 1 != n && (charArr[i + 1] == 'V' || charArr[i + 1] == 'X')) {
                        result -= x;
                        break;
                    }
                    result += x;
                    break;
                case 'V':
                    x = 5;
                    result += x;
                    break;
                case 'X':
                    x = 10;
                    // subtraction cases
                    if (i + 1 != n && (charArr[i + 1] == 'L' || charArr[i + 1] == 'C')) {
                        result -= x;
                        break;
                    }
                    result += x;
                    break;
                case 'L':
                    x = 50;
                    result += x;
                    break;
                case 'C':
                    x = 100;
                    // subtraction cases
                    if (i + 1 != n && (charArr[i + 1] == 'D' || charArr[i + 1] == 'M')) {
                        result -= x;
                        break;
                    }
                    result += x;
                    break;
                case 'D':
                    x = 500;
                    result += x;
                    break;
                case 'M':
                    x = 1000;
                    result += x;
                    break;
                default:
                    break;
            }

        }
        return result;
    }
}
