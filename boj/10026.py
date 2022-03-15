import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, item, visit, flag):

    X = [-1, 1, 0, 0]
    Y = [0, 0, -1, 1]

    visit[x][y] = True

    # 상, 하, 좌, 우 조회
    for i in range(4):
        vx = x + X[i]
        vy = y + Y[i]

        if 0 <= vx < N and 0 <= vy < N:
            
            # 방문하지 않은 경우
            if visit[vx][vy] != True:
                
                # 적록색약일 경우
                if flag == True and item in 'RG':

                    # R과 G를 구분하지 못함
                    if MAP[vx][vy] in 'RG':
                        dfs(vx, vy, item, visit, flag)
                
                # 적록색약이 아닐 경우
                else:
                    if MAP[vx][vy] == item:
                        dfs(vx, vy, item, visit, flag)

N = int(input())
MAP = [list(input()) for _ in range(N)]

# 적록색약이 없는 경우
visit = [[False] * N for _ in range(N)]
no = 0
for item in 'RGB':
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == item and visit[i][j] != True:
                dfs(i, j, item, visit, False)
                no += 1

# 적록색약이 있는 경우
visit = [[False] * N for _ in range(N)]
yes = 0
for item in 'RGB':
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == item and visit[i][j] != True:
                dfs(i, j, item, visit, True)
                yes += 1

print(no, yes)