package com.stephenclhc;

public class BinarySearch {
    // 704 BinarySearch

    public int search(int[] nums, int target) {
        int leftIndex = 0;
        int rightIndex = nums.length - 1;

        while (leftIndex <= rightIndex) {
            int middleIndex = (leftIndex + rightIndex) / 2; // middleIndex = leftIndex + (leftIndex + rightIndex) / 2
            if(nums[middleIndex] == target) return middleIndex;
            if(nums[middleIndex] < target)
                leftIndex = middleIndex + 1;
            else rightIndex = middleIndex - 1;
        }
        return -1;
    }
}
