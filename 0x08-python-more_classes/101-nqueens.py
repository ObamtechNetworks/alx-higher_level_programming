#!/usr/bin/python3
"""This module defines a program that solves the
N queens puzzle challenge.
The N queens puzzle is the challenge of placing N non-attacking queens
on an NxN chessboard.

"""


import sys

# get command line arguments
args = sys.argv  # command line argument
arg_count = len(args)  # number of argument

# check for number of arguments if valid
if arg_count != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = args[1]
# check if N is an integer
try:
    N = int(N)
except Exception:
    print("N must be a number")
    sys.exit(1)

if not N >= 4:
    print("N must be at least 4")
    sys.exit(1)

# IF ALL PASS, PRINT THE SOLUTIONS TO THE PROBLEM
# create board based on N


def can_place_queen(board, row, col):
    """checks if a queen can be placed in
    the given column of the current row

    Args:
        board: the board to check its rows, cols
        row: the row of the board
        col: the column of the board
    """

    for i in range(row):
        # Check the column
        if board[i][col] == 1:
            return False

        # Check upper left diagonal
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False

        # Check upper right diagonal
        if col + (row - i) < len(board) and board[i][col + (row - i)] == 1:
            return False

    return True


# Recursive function to solve N-Queens problem using backtracking
def solve_n_queens_helper(N, board, row):
    """Solves the N queens puzzle through backtracking

    Args:
        N: the given Number of queen
        board: the board to place queens
        row: each row in the board
    """

    if row == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return

    for col in range(N):
        if can_place_queen(board, row, col):
            board[row][col] = 1
            solve_n_queens_helper(N, board, row + 1)
            board[row][col] = 0


# Function to initiate the solving process and print solutions
def solve_n_queens(N):
    """Calls the helper functions to solve the solutions

    Args
        N: the given Number of queen to solve for
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_n_queens_helper(N, board, 0)


# Call the function to solve N-Queens problem
solve_n_queens(N)
