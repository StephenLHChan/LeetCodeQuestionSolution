# 931. Minimum Falling Path Sum

def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(1, rows):
        for col in range(cols):

            if col == 0:
                matrix[row][col] += min(matrix[row - 1]
                                        [col], matrix[row - 1][col + 1])
            elif col == cols - 1:
                matrix[row][col] += min(matrix[row - 1]
                                        [col - 1], matrix[row - 1][col])
            else:
                matrix[row][col] += min(matrix[row - 1][col - 1],
                                        matrix[row - 1][col], matrix[row - 1][col + 1])

    return min(matrix[-1])
