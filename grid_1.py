from typing import List


def solve(grid: List[List[str]]):
    memo_grid = [[None] * len(grid[0]) for row in range(len(grid))]
    dfs(0, 0, grid, memo_grid)
    return memo_grid[0][0]


def dfs(row_index, column_index, grid, memo_grid):
    if row_index == len(grid) or column_index == len(grid[0]):
        return 0

    if grid[row_index][column_index] == '#':
        return 0

    if row_index == len(grid) - 1 and column_index == len(grid[0]) - 1:
        return 1

    if memo_grid[row_index][column_index] is not None:
        return memo_grid[row_index][column_index]

    memo_grid[row_index][column_index] = 0
    for row_direction, column_direction in [[1, 0], [0, 1]]:
        memo_grid[row_index][column_index] += dfs(row_index + row_direction, column_index + column_direction, grid, memo_grid)

    return memo_grid[row_index][column_index]


if __name__ == '__main__':
    grid = [
        ['.', '.', '.', '#'],
        ['.', '#', '.', '.'],
        ['.', '.', '.', '.']
    ]
    print(solve(grid))