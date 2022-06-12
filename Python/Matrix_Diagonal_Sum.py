# 1572. Matrix Diagonal Sum

def diagonalSum(self, mat: List[List[int]]) -> int:
    left_index = 0
    right_index = -1
    sum = 0
    for row in mat:
        sum += row[left_index]
        sum += row[right_index]
        left_index += 1
        right_index -= 1

    if len(mat) % 2 == 1:
        mid = len(mat) // 2
        sum -= mat[mid][mid]
    return sum
