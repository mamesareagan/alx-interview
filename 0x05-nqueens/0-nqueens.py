#!/usr/bin/python3
''' N Queens
'''
import sys


def print_board(board):
    '''Prints the board
    '''
    result = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                result.append([i, j])
    print(result)


def is_safe(board, row, col):
    '''Checks if it's safe to place a queen
    '''
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve(board, col):
    '''Solves the N Queen problem using Backtracking
    '''
    if col == len(board):
        print_board(board)
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve(board, col + 1) or res
            board[i][col] = 0
    return res


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    if N < 4:
        print('N must be at least 4')
        sys.exit(1)
    board = [[0 for j in range(N)] for i in range(N)]
    solve(board, 0)
