# 279. Perfect Squares

def numSquares(self, n: int) -> int:
    squares = [n ** 2 for n in range(0, int(sqrt(n)) + 1)]
    res = [float('inf')] * (n + 1)

    res[0] = 0

    for i in range(1, n + 1):
        for square in squares:
            if i < square:
                break
            res[i] = min(res[i], res[i - square] + 1)

    return res[-1]
