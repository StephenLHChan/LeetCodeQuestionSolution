// 1512. Number of Good Pairs

var numIdenticalPairs = function(nums) {
    let count = 0;
    for(let i = 0; i < nums.length; i++){
        for(let j = 1; j < nums.length ; j++){
            if (nums[i] === nums[j] && i < j) count++;
        }
    }
    return count;
};

var numIdenticalPairs = function(nums) {
    let map = {};
    let count = 0;
    for(let i = 0; i < nums.length; i++){
        if(map[nums[i]]){
            count += map[nums[i]];
            map[nums[i]]++;
        } else {
            map[nums[i]] = 1;
        }
    }
    return count;
};