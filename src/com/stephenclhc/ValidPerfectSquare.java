package com.stephenclhc;

public class ValidPerfectSquare {
    // 367. Valid Perfect Square
    public boolean isPerfectSquare(int num) {
        long left = 1;
        long right = num;

        if (num == 1)
            return true;

        while(left < right){
            long mid = left + (right - left) / 2; //since the calculation involved mid * mid, using int may be overflow
            if (mid * mid == num)
                return true;
            if (mid * mid < num)
                left = mid + 1;
            else right = mid - 1;
        }
        return false;
    }
}
