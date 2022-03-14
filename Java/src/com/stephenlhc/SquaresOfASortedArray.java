package com.stephenlhc;

public class SquaresOfASortedArray {
    // 977. Squares of a Sorted Array

    public int[] sortedSquares(int[] nums) {
        var result = new int[nums.length];

        int head = 0;
        int tail = nums.length - 1;

        for(int i = nums.length - 1; i >= 0; i--){
            if(Math.abs(nums[head]) > Math.abs(nums[tail])) {
                result[i] = nums[head] * nums[head];
                head++;
            }
            else{
                result[i] = nums[tail] * nums[tail];
                tail--;
            }
        }
        return result;
    }
}
