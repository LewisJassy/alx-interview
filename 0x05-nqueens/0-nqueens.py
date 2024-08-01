#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """
    Checks if it is safe to place a queen at position (row, col) on the board.

    Args:
        board (list of lists): The current state of the board.
        row (int): The row index of the position to check.
        col (int): The column index of the position to check.
        N (int): The size of the board.

    Returns:
        bool: True if it is safe to place a queen
        at the position, False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve(board, col, N, solutions):
    """
    Recursively solves the N-Queens problem by placing queens on the board.

    Args:
        board (list of lists): The current state of the board.
        col (int): The current column index.
        N (int): The size of the board.
        solutions (list): A list to store the solutions.

    Returns:
        None
    """
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve(board, col + 1, N, solutions)
            board[i][col] = 0


def nqueens(N):
    """
    Solves the N-Queens problem and prints all solutions.

    Args:
        N (int): The size of the board.

    Returns:
        None
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve(board, 0, N, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)
