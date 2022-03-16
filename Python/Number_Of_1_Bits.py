# 191. Number of 1 Bits

def hammingWeight(self, n: int) -> int:
    count = 0
    for char in str(bin(n)):
        if char == '1':
            count += 1
    return count
