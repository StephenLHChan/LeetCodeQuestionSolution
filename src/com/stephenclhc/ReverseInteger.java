package com.stephenclhc;

public class ReverseInteger {
    // 7. Reverse Integer

    public int reverse(int x) {
        boolean isNegative =  x < 0;

        x = Math.abs(x);

        int result = 0;
        while (x > 0){
            //It is a 32-bit integer. to check if it is larger or smaller than the limits
            if(result > Integer.MAX_VALUE / 10 ||
                    (-result < Integer.MIN_VALUE /10 && isNegative))
                return 0;
            result = result * 10 + x%10;
            x/= 10;
        }

        if (isNegative)
            return  - result;
        else return result;
    }
}
