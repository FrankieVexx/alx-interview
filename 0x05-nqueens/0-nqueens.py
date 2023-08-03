#!/usr/bin/python3

"""solving nqueens problem in python"""


import sys


# error handling for argv[1]

if __name__ == "__main__":
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)
    N = sys.argv[1]
    try:
        N_int = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N_int < 4:
        print("N must be at least 4")
        sys.exit(1)

# creates array of queen positions
    coords = []

    def is_safe(coords, row, col):
        """ Checks if queen can be placed in coord of board.
        Returns True if can, else False
        """
        rows = []
        colms = []
        diag_r = []
        diag_l = []

        for square in coords:
            rows.append(square[0])
            colms.append(square[1])
            diag_r.append(square[0] + square[1])
            diag_l.append(square[1] - square[0])

        if row in rows or col in colms:
            return False
        if row + col in diag_r or col - row in diag_l:
            return False

        return True

    def solve_nqueens(coords, col, safe_queens=[]):
        """ Creates array of queen positions
        Returns array
        """
        for x in range(N_int):
            if is_safe(coords, x, col):
                coords.append([x, col])
                if col == N_int - 1:
                    safe_queens.append(coords.copy())
                    del coords[-1]
                else:
                    solve_nqueens(coords, col + 1)

        if len(coords):
            del coords[-1]
        return safe_queens

# sets base case for recursion

    coords = solve_nqueens(coords, 0)

# prints coords of squares for safe queens

    for squares in coords:
        print(squares)
