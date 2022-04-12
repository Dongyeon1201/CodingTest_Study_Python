X = [-1, 1, 0, 0]
Y = [0, 0, -1, 1]

MAX = 0


def dfs(x, y, alphabet, count):

    global MAX
    MAX = max(MAX, count)

    for i in range(4):
        vx = x + X[i]
        vy = y + Y[i]

        if 0 <= vx < R and 0 <= vy < C:
            if MAP[vx][vy] not in alphabet:
                alphabet.add(MAP[vx][vy])
                dfs(vx, vy, alphabet, count + 1)
                alphabet.remove(MAP[vx][vy])


R, C = map(int, input().split())
MAP = [list(input()) for _ in range(R)]
alphabet = set()
alphabet.add(MAP[0][0])
dfs(0, 0, alphabet, 1)
print(MAX)
