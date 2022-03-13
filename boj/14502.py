from collections import deque
from copy import deepcopy
from itertools import combinations

def bfs(map):

    X = [-1, 1, 0, 0]
    Y = [0, 0, -1, 1]
    count = 0

    # 이미 바이러스가 존재하는 좌표를 큐에 넣는다.
    queue = deque(START)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            
            # 새로운 좌표(상, 하, 좌, 우)
            vx = x+X[i]
            vy = y+Y[i]

            # 연구소를 벗어나지 않을 때
            if 0 <= vx < N and 0 <= vy < M:

                # 인접한 공간이 벽이 아닌 공간일 때
                if map[vx][vy] == 0:

                    # 바이러스 전파
                    map[vx][vy] = 2

                    # 큐에 추가
                    queue.append((vx, vy))

    # 모든 바이러스가 퍼진 후 안전지대(0) 갯수 확인
    for i in range(N):
        for j in range(M):
            if map[i][j] == 0:
                count += 1

    # 안전지대 갯수 반환
    return count

# 가로, 세로 길이 받기
N, M = map(int, input().split())

# 초기 연구소 상태 받아오기
MAP = [list(map(int, input().split())) for _ in range(N)]

# 바이러스가 이미 존재하는 위치(2)
START = []

# 바이러스가 아직 퍼지지 않은 연구소 구역(0)
ZERO = []

# 가장 큰 안전지대 크기를 저장할 변수
max = 0

# 바이러스 위치와 아직 안전한 위치 확인
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0: ZERO.append((i, j))
        if MAP[i][j] == 2: START.append((i, j))

# 아직 안전한 위치의 조합을 구하여 벽을 세울 수 있는 조합 확인
WALL = list(combinations(ZERO, 3))

for item in WALL:

    map = deepcopy(MAP)

    # 벽 위치에 값을 0 -> 1로 변경
    for k in item:
        x, y = k
        map[x][y] = 1
    
    # 벽을 추가로 세운 연구소 정보를 사용하여 bfs 동작
    count = bfs(map)

    # 반환받은 안전지대 갯수가 가장 많을 경우 max 변경
    if max < count:
        max = count

print(max)