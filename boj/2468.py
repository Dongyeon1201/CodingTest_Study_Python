import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, W, visit):

    X = [-1, 1, 0, 0]
    Y = [0, 0, -1, 1]

    visit[x][y] = True

    # 상, 하, 좌, 우 좌표 확인
    for i in range(4):
        vx = x + X[i]
        vy = y + Y[i]

        # 지역을 벗어나는 좌표인지 확인
        if 0 <= vx < N and 0 <= vy < N:

            # 잠기는 수위가 아닌지 확인 & 이미 확인한 좌표인지 확인
            if MAP[vx][vy] > W and visit[vx][vy] != True:
                dfs(vx, vy, w, visit)

N = int(input())

MAP = [list(map(int, input().split())) for _ in range(N)]

# 비가 안오는 경우도 존재하며, 이때는 무조건 안전지대가 1개는 생긴다.
MAX = 1

# 바닷물 높이 1 ~ N
for w in range(1, 101):

    visit = [[False] * N for _ in range(N)]
    count = 0

    # 모든 좌표를 시작점으로 조회
    for i in range(N):
        for j in range(N):

            # 잠기지 않은 부분일 경우
            if MAP[i][j] > w and visit[i][j] != True:
                dfs(i, j, w, visit)
                count += 1

    if MAX < count: MAX = count

print(MAX)