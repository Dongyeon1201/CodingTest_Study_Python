import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, block, visit):

    X = [-1, 1, 0, 0]
    Y = [0, 0, -1, 1]

    visit[x][y] = True
    count = 1

    for i in range(4):
        vx = x + X[i]
        vy = y + Y[i]

        # 영역을 벗어나지 않을 경우
        if 0 <= vx < M and 0 <= vy < N:
            if visit[vx][vy] == False:
                count += dfs(vx, vy, block, visit)

    return count

M, N, K = map(int, input().split())
block = []
divide_count = 0
result = []
visit = [[False] * (N+1) for _ in range(M+1)]

for _ in range(K):
    # sx : 시작 x 좌표 (왼쪽 아래)
    # sy : 시작 y 좌표 (왼쪽 아래)
    # ex : 끝 x 좌표 (오른쪽 위)
    # ey : 끝 y 좌표 (오른쪽 위)
    sx, sy, ex, ey = map(int, input().split())

    # 직사각형 부분 저장(-1)
    for i in range(sy, ey):
        for j in range(sx, ex):
            visit[i][j] = -1

# 모든 좌표 조회
for i in range(M):
    for j in range(N):

        # 직사각형 부분이 아니며, 방문하지 않은 부분일 때
        if not (i, j) in block and visit[i][j] == False:

            # 깊이 탐색 진행 & 탐색 시 공간의 넓이 반환
            result.append(dfs(i, j, block, visit))

            # 깊이 탐색 진행 횟수 = 분리된 공간 개수
            divide_count += 1

print(divide_count)
print(*sorted(result))