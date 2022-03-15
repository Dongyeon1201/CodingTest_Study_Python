import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, visit):

    X = [-1, 0, 1]
    Y = [-1, 0, 1]

    visit[x][y] = True

    for item_x in X:
        for item_y in Y:
            vx = x + item_x
            vy = y + item_y

            if vx == x and vy == y:
                continue

            if 0 <= vx < H and 0 <= vy < W:
                if MAP[vx][vy] == 1 and visit[vx][vy] != True:
                    dfs(vx, vy, visit)

result = []

while True:
    W, H = map(int, input().split())
    count = 0

    if W == 0 and H == 0:
        break

    MAP = [list(map(int, input().split())) for _ in range(H)]
    VISIT = [[False] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if MAP[i][j] == 1 and VISIT[i][j] != True:                
                dfs(i, j, VISIT)
                count += 1

    result.append(count)

for item in result:
    print(item)