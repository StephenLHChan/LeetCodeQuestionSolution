# 64. Minimum Path Sum

def minPathSum(self, grid: List[List[int]]) -> int:
    sumOfPath = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    sumOfPath[0][0] = grid[0][0]

    for col in range(1, len(grid[0])):
        sumOfPath[0][col] = sumOfPath[0][col - 1] + grid[0][col]

    for rol in range(1, len(grid)):
        sumOfPath[rol][0] = sumOfPath[rol - 1][0] + grid[rol][0]

    for rol in range(1, len(grid)):
        for col in range(1, len(grid[0])):
            from_top = sumOfPath[rol - 1][col] + grid[rol][col]
            from_left = sumOfPath[rol][col - 1] + grid[rol][col]
            sumOfPath[rol][col] = min(from_top, from_left)

    return sumOfPath[-1][-1]
