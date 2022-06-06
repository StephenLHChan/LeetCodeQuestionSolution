// 1930. Unique Length-3 Palindromic Subsequences

var countPalindromicSubsequence = function(s) {
    const unique_chars = [...new Set(s.split(''))];
    
    return unique_chars.reduce((count, ch)=>{
        const first_one = s.indexOf(ch);
        const last_one = s.lastIndexOf(ch);
        if (last_one > first_one)
            return count + new Set(s.slice(first_one + 1, last_one)).size
        else return count
    }, 0)   
};