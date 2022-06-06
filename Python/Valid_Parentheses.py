# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        pare = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for ch in s:
            if ch in pare.keys():
                stack.append(ch)
            elif len(stack) == 0 or ch != pare[stack.pop()]:
                return False
        return len(stack) == 0
