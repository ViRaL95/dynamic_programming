from typing import List
from pprint import pprint

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



def dp_way(grid):
    dp_grid = [[0] * len(grid[0]) for row in grid]


    row_blocked, column_blocked = False, False
    for row_index in range(len(grid) - 1, -1, -1):
        for column_index in range(len(grid[0]) - 1, -1, -1):
            if row_index == len(grid) - 1:
                if grid[row_index][column_index] == '#':
                    row_blocked = True
                if not row_blocked:
                    dp_grid[row_index][column_index] = 1
                else:
                    dp_grid[row_index][column_index] = 0

            if column_index == len(grid[0]) - 1:
                if grid[row_index][column_index] == '#':
                    column_blocked = True

                if not column_blocked:
                    dp_grid[row_index][column_index] = 1

                else:
                    dp_grid[row_index][column_index] = 0

    print(dp_grid)

    for row_index in range(len(grid) - 2, -1, - 1):
        for column_index in range(len(grid[0]) - 2, - 1, -1):
            if grid[row_index][column_index] == '#':
                dp_grid[row_index][column_index] = 0
            else:
                dp_grid[row_index][column_index] = dp_grid[row_index + 1][column_index] + dp_grid[row_index][column_index + 1]

    print(dp_grid)
    return dp_grid[0][0]


if __name__ == '__main__':
    grid = [['.'] * 20 for row in range(1, 21)]

    print(len(grid), len(grid[0]))
    print((dp_way(grid)))
