package com.stephenclhc;

public class SearchInsertPosition {
    // 35. Search Insert Position

    public int searchInsert(int[] nums, int target){
        int leftIndex = 0;
        int rightIndex = nums.length;
        int middleIndex;

        if(target > nums[nums.length - 1])
            return nums.length;

        while (leftIndex <= rightIndex){
            middleIndex = leftIndex + (rightIndex - leftIndex) / 2;
            if (nums[middleIndex] == target)
                return middleIndex;
            if (nums[middleIndex] < target)
                leftIndex = middleIndex + 1;
            else rightIndex = middleIndex - 1;
        }
        return leftIndex;
    }

}
