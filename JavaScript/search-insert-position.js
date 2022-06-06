// 35. Search Insert Position

var searchInsert = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right){
        let mid = left + Math.floor((right - left) / 2);
        if (target > nums[mid - 1] && target <= nums[mid]) return mid;
        if(target < nums[left]) return left;
        if(target > nums[right]) return right + 1;
        if (target > nums[mid]) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
};