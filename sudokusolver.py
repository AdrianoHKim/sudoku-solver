import numpy as np
import time

grid = [[2, 0, 0, 0, 0, 3, 1, 0, 0],  # example from sudoku.com (0 = empty space to guess).
        [6, 0, 7, 0, 1, 5, 3, 4, 0],
        [0, 0, 0, 0, 2, 0, 5, 0, 8],
        [0, 0, 9, 1, 3, 0, 6, 8, 0],
        [0, 3, 8, 7, 0, 4, 2, 1, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 4],
        [0, 9, 0, 2, 5, 0, 0, 0, 0],
        [0, 2, 6, 3, 0, 0, 0, 0, 1],
        [3, 4, 0, 8, 0, 0, 9, 2, 6]]

print(np.matrix(grid))
time.sleep(2)


def possible(row, column, number):
    global grid
    # Is the number appearing in the given row?
    for i in range(0, 9):
        if grid[row][i] == number:
            return False

    # Is the number appearing in the given column?
    for i in range(0, 9):
        if grid[i][column] == number:
            return False

    # Is the number appearing in the given square?
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == number:
                return False

    return True


def solve():
    global grid
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0

                return

    print('Solution: ')
    time.sleep(2)
    print(np.matrix(grid))
    time.sleep(2)
    input('Press enter to see more possible solutions, if there is no more solutions, this program will finish.')


solve()
