#!/usr/bin/python3
"""
N Queens solution module
"""
import sys

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_nqueens(N, board, col, solutions):
    if col == N:
        solutions.append(board[:])
        return

    for i in range(N):
        if is_safe(board, i, col):
            board[col] = i
            solve_nqueens(N, board, col + 1, solutions)

def print_solutions(N, solutions):
    for solution in solutions:
        for row in range(N):
            print([row, solution[row]])
        print()

def main():
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

    board = [-1] * N
    solutions = []
    solve_nqueens(N, board, 0, solutions)
    print_solutions(N, solutions)

if __name__ == "__main__":
    main()

