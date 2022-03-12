from collections import deque

def bfs(TOMATO, START, M, N, H):

    X = [-1, 1, 0, 0]
    Y = [0, 0, -1, 1]
    Z = [-1, 1]

    queue = deque(START)

    days = -1

    # 더 이상 추가 변화가 없을 때
    while queue:
        
        # for문으로 반복하여, 이전에 큐에 쌓인 모든 값(1일 변화량)을 모두 처리한다.
        for _ in range(len(queue)):

            z, y, x = queue.popleft()

            # 앞/뒤
            for i in range(2):
                # 토마토 창고의 범위를 벗어난 좌표인지 확인
                if z+Z[i] < 0 or z+Z[i] >= H:
                    continue
                
                # 토마토가 들어있지 않은 칸(-1)의 좌표인지 확인
                elif TOMATO[z+Z[i]][y][x] == -1:
                    continue

                # 토마토가 익지 않은 상태(0)이어야 한다.
                elif TOMATO[z+Z[i]][y][x] == 0:
                    TOMATO[z+Z[i]][y][x] = 1
                    queue.append((z+Z[i], y, x))

            # 상/하/좌/우
            for i in range(4):
                # 토마토 창고의 범위를 벗어난 좌표인지 확인
                if x+X[i] < 0 or x+X[i] >= M or y+Y[i] < 0 or y+Y[i] >= N:
                    continue
                
                # 토마토가 들어있지 않은 칸(-1)의 좌표인지 확인
                elif TOMATO[z][y+Y[i]][x+X[i]] == -1:
                    continue

                # 토마토가 익지 않은 상태(0)이어야 한다.
                elif TOMATO[z][y+Y[i]][x+X[i]] == 0:
                    TOMATO[z][y+Y[i]][x+X[i]] = 1
                    queue.append((z, y+Y[i], x+X[i]))
        
        days += 1
    
    # 모든 작업이 끝났지만, 아직도 익지 않은 토마토 -> 고립된 토마토 존재
    for i in TOMATO:
        for j in i:
            for k in j:
                if k == 0:
                    return -1

    return days

M, N, H = map(int, input().split())

TOMATO = []
for _ in range(H):

    LINE = []
    for _ in range(N):
        LINE.append(list(map(int, input().split())))
    
    TOMATO.append(LINE)

START = []

# 연결되지 않은 토마토 존재 여부와 이미 익은 토마토 확인
for h in range(H):
    for i in range(N):
        for j in range(M):

            # 이미 익은 상태인 토마토 기록
            if TOMATO[h][i][j] == 1: 
                START.append((h, i, j))
            
print(bfs(TOMATO, START, M, N, H))