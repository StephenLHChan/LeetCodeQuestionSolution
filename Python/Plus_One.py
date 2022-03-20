# 66. Plus One

def plusOne(self, digits: List[int]) -> List[int]:
    for i in reversed(range(len(digits))):
        digits[i] += 1
        if digits[i] != 10:
            return digits
        else:
            digits[i] %= 10

    result = [1]
    return result + digits
