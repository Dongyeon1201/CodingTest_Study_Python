import sys

sys.setrecursionlimit(10 ** 6)

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

# 이미 탐색한 경로에 대해 도달 가능한 경로 갯수를 저장
# 초기값을 0으로 설정하는 경우 아래 2가지 경우가 겹친다.
# 1. 탐색을 하기 전 상태(초기 값 0)일경우
# 2. 탐색을 하였지만, 목표지점에 도달하는 경우가 없어서 0일경우
# 따라서 2번의 경우에도, 1번의 경우로 생각하고 계속 탐색을 반복하는 경우가 생긴다. 따라서 초기값을 0이 아닌 다른 값으로 설정해야한다.
dp = [[-1] * N for _ in range(M)]


def dfs(x, y):

    X = [1, -1, 0, 0]
    Y = [0, 0, 1, -1]

    if (x, y) == (M - 1, N - 1):
        return 1

    # 이미 탐색한 경로가 존재한 경우
    if dp[x][y] != -1:
        return dp[x][y]

    # 합계 계산을 위해 0으로 변경
    dp[x][y] = 0

    # 상하좌우 탐색
    for i in range(4):
        vx = x + X[i]
        vy = y + Y[i]

        # 범위를 넘어서지 않는 경우
        if 0 <= vx < M and 0 <= vy < N:

            # 더 작은 구간만 이동
            if board[x][y] > board[vx][vy]:

                # 현재 위치에서 이동할 수 있는 경로 갯수 누적
                dp[x][y] += dfs(vx, vy)

    return dp[x][y]


dfs(0, 0)
print(dp[0][0])

"""
4 5
50 45 37 100 30
35 50 40 100 25
100 100 100 100 28
27 24 22 15 10
"""
