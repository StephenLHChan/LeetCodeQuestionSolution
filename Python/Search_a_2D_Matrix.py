# 74. Search a 2D Matrix

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])

    left = 0
    right = m * n - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_item = matrix[mid // n][mid % n]
        if target == mid_item:
            return True
        if target < mid_item:
            right = mid - 1
        else:
            left = mid + 1
    return False
