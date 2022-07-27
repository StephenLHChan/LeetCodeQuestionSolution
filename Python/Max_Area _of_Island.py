# 695. Max Area of Island

def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    def search(grid, row, col, visited):
        rowInbound = row >= 0 and row < len(grid)
        colInbound = col >= 0 and col < len(grid[0])
        if not rowInbound or not colInbound:
            return 0

        pos = str(row) + ',' + str(col)
        if pos in visited:
            return 0
        visited.add(pos)

        if grid[row][col] == 0:
            return 0
        if grid[row][col] == 1:
            return 1 + search(grid, row + 1, col, visited) + search(grid, row - 1, col, visited) + search(grid, row, col + 1, visited) + search(grid, row, col - 1, visited)

    res = 0
    visited = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            res = max(search(grid, row, col, visited), res)
    return res
