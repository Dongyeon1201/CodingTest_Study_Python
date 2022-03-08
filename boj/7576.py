from collections import deque

def bfs(TOMATO, START, M, N):

    X = [-1, 1, 0, 0]
    Y = [0, 0, -1, 1]

    queue = deque(START)

    days = -1

    # 더 이상 추가 변화가 없을 때
    while queue:
        
        # for문으로 반복하여, 이전에 큐에 쌓인 모든 값(1일 변화량)을 모두 처리한다.
        for _ in range(len(queue)):

            y, x = queue.popleft()

            for i in range(4):

                if x+X[i] < 0 or x+X[i] >= M or y+Y[i] < 0 or y+Y[i] >= N:
                    continue
                
                elif TOMATO[y+Y[i]][x+X[i]] == -1:
                    continue

                elif TOMATO[y+Y[i]][x+X[i]] == 0:
                    TOMATO[y+Y[i]][x+X[i]] = 1
                    queue.append((y+Y[i], x+X[i]))
        
        days += 1
    
    # 모든 작업이 끝났지만, 아직도 익지 않은 토마토 -> 고립된 토마토 존재
    for i in TOMATO:
        for j in i:
            if j == 0:
                return -1

    return days

M, N = map(int, input().split())

TOMATO = []

for _ in range(N):
    TOMATO.append(list(map(int, input().split())))

START = []

# 연결되지 않은 토마토 존재 여부와 이미 익은 토마토 확인
for i in range(N):
    for j in range(M):
            
        # 이미 익은 상태인 토마토 기록
        if TOMATO[i][j] == 1: 
            START.append((i, j))
            
print(bfs(TOMATO, START, M, N))