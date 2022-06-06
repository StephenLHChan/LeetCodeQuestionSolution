// 9. Palindrome Number

var isPalindrome = function(x) {
    if (x < 0 || (x > 0 && x % 10 === 0)) return false;
    const input = x;
    let rev = 0;
    while (x > 0) {
        rev = rev * 10 + (x % 10);
        x = Math.floor(x / 10);
    }
    return input === rev;
 
};