package com.stephenclhc;

import java.util.HashMap;
import java.util.Map;

public class TwoSumII {
    // 167. Two Sum II - Input Array Is Sorted


    //Solution 1: use HashMap
    public int[] twoSum(int[] numbers, int target){
        Map<Integer,Integer> map = new HashMap<>();

        for(int i = 0; i < numbers.length; i++){
            if(map.containsKey(target - numbers[i])){
                return new int[]{map.get(target - numbers[i]) , i + 1};
            } else
                map.put(numbers[i], i + 1);
        }
        return null;
    }

    //Solution 2:
    public int[] twoSum2(int[] numbers, int target){
        int firstIndex = 0;
        int lastIndex = numbers.length - 1;

        while(firstIndex < lastIndex) {
            int sum = numbers[firstIndex] + numbers[lastIndex];

            if(sum == target)
                return new int[] {firstIndex + 1, lastIndex + 1};

            if(sum > target)
                lastIndex--;
            else firstIndex++;
        }
        return null;
    }


}
