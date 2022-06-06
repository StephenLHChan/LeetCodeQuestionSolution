// 696. Count Binary Substrings

var countBinarySubstrings = function(s) {
    let currentCount = 1;
    let prevCount = 0;
    let ans = 0;
    for (let i = 1; i < s.length; i++)
        if (s[i] === s[i-1]) 
            currentCount++;
        else {
            ans += Math.min(currentCount, prevCount);
            prevCount = currentCount;
            currentCount = 1;
        }
    return ans + Math.min(currentCount, prevCount)
};
