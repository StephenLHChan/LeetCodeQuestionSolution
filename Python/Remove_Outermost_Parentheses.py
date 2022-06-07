# 1021. Remove Outermost Parentheses

def removeOuterParentheses(self, s: str) -> str:
    result = []
    count = 0
    for item in s:
        if item == '(':
            if count > 0:
                result.append(item)
            count += 1
        else:
            count -= 1
            if count > 0:
                result.append(item)
    return ''.join(result)
