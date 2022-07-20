# 120. Triangle

def minimumTotal(self, triangle: List[List[int]]) -> int:
    for rol in range(1, len(triangle)):
        for col in range(rol + 1):
            if col == 0:
                triangle[rol][col] += triangle[rol - 1][col]
            elif col == len(triangle[rol]) - 1:
                triangle[rol][col] += triangle[rol - 1][col - 1]
            else:
                triangle[rol][col] += min(triangle[rol - 1]
                                          [col - 1], triangle[rol - 1][col])
    return min(triangle[-1])
