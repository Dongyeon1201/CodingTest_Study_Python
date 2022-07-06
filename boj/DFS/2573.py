import sys
from collections import deque

input = sys.stdin.readline

# pypy3에서 메모리 초과 발생 가능
# 10 ** 6과 같이 너무 큰 수를 설정하면, 미리 스택 메모리의 영역을 설정하기 때문에 메모리 초과 발생이 가능하다.
# sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
years = 0

X = [1, -1, 0, 0]
Y = [0, 0, 1, -1]


def bfs(x, y):

    visit[x][y] = True
    queue = deque([(x, y)])
    melt_list = []

    while queue:
        nx, ny = queue.popleft()
        melt_count = 0

        for i in range(4):
            vx = nx + X[i]
            vy = ny + Y[i]

            if 0 <= vx < N and 0 <= vy < M:
                if board[vx][vy] > 0 and visit[vx][vy] == False:
                    visit[vx][vy] = True
                    queue.append((vx, vy))

                # 탐색하며 주변 바다도 확인
                elif board[vx][vy] == 0:
                    melt_count += 1

        # 높이를 낮춰야하는 빙산의 정보만 저장 후, 반환
        # 처음에는 맵의 크기만큼 2차원 배열을 만들어 낮추는 높이를 저장했지만, 메모리 영역을 아낄 수 있다.
        if melt_count > 0:
            melt_list.append([nx, ny, melt_count])

    return melt_list


while True:
    visit = [[False] * M for _ in range(N)]
    count = 0

    # 빙산 덩어리 갯수 확인
    for x in range(1, N - 1):
        for y in range(1, M - 1):
            if board[x][y] > 0 and visit[x][y] == False:
                count += 1
                melt_list = bfs(x, y)

    # 빙산이 여러 덩어리 나눠져있을 때
    if count > 1:
        print(years)
        break

    # 빙산이 없을 때
    elif count == 0:
        print(0)
        break

    # 빙산 높이 낮추기
    for x, y, count in melt_list:
        board[x][y] -= count
        board[x][y] = max(board[x][y], 0)

    years += 1
