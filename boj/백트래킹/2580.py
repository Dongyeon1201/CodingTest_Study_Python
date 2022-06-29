import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
info = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]


def print_board():
    for i in range(9):
        print(*board[i])


def check(x, y, value):

    # 같은 행 확인
    if value in board[x]:
        return False

    # 같은 열 확인
    if value in list(zip(*board))[y]:
        return False

    # 해당 좌표가 속하는 3x3 부분 확인
    rectangle = list(zip(*board[(x // 3) * 3 : (x // 3 + 1) * 3]))[
        (y // 3) * 3 : (y // 3 + 1) * 3
    ]

    for l in rectangle:
        if value in l:
            return False

    return True


def dfs(depth):

    if depth == len(info):
        print_board()
        exit(0)

    for i in range(1, 10):
        if check(info[depth][0], info[depth][1], i):
            board[info[depth][0]][info[depth][1]] = i
            dfs(depth + 1)
            board[info[depth][0]][info[depth][1]] = 0


dfs(0)
