// 1. Two Sum

var twoSum = function(nums, target) {
    const seen = new Map();
    for (let i = 0; i < nums.length; i++){
        if(seen.has(target - nums[i])){
            return [i, seen.get(target - nums[i])]
        } else {
            seen.set(nums[i] , i)
        }
    }    
};