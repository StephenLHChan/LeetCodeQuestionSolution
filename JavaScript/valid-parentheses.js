// 20. Valid Parentheses

var isValid = function(s) {
    if (s.length % 2 !== 0) return false

    const chars = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    const stack = []

    for (let i = 0; i < s.length; i++) {
        if (chars[s[i]]) {
            if (chars[s[i]] === stack[stack.length - 1]) {
                stack.pop()
            } else {
                return false
            }
        } else {
            stack.push(s[i])
        }
    }

    return !stack.length 
};
