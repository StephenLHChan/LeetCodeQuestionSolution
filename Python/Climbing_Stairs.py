# 70. Climbing Stairs

def climbStairs(self, n: int) -> int:
    s = [1, 2] + [0 for i in range(2, n)]
    for i in range(2, n):
        s[i] = s[i-1] + s[i-2]
    return s[n - 1]
