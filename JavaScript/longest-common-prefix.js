// 14. Longest Common Prefix

var longestCommonPrefix = function(strs) {
    for (let i = 0; i < strs[0].length; i++){
        for (let j = 1; j < strs.length; j++){
            if(strs[j][i] !== strs[0][i])
                return strs[0].slice(0, i);
        }
    }
    return strs[0];
};