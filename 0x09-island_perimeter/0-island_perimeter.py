#!/usr/bin/python3
"""Solving island perimeter problem"""


def check_value(x):
    """checking if value is 0 or 1
    """
    if (x == 0):
        return 1
    return 0


def island_perimeter(grid):
    """Solution to island perimeter problem
    """

    row = len(grid)
    col = len(grid[0])
    assert (1 <= row and col <= 100), "length must be between 1 an 100"

    x = 0
    for i in range(row):
        for j in range(col):
            assert (grid[i][j] == 0) or (grid[i][j] == 1),\
                "grid numbers must be 0 or 1"
            if grid[i][j] == 1:
                if i-1 < 0:
                    x += 1
                else:
                    x += check_value(grid[i-1][j])
                if j-1 < 0:
                    x += 1
                else:
                    x += check_value(grid[i][j-1])

                try:
                    x += check_value(grid[i+1][j])
                except IndexError:
                    x += 1
                try:
                    x += check_value(grid[i][j+1])
                except IndexError:
                    x += 1

    return x
