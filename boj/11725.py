import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())

MAP = [[] for _ in range(N + 1)]
result = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    MAP[a].append(b)
    MAP[b].append(a)

visit = [False] * (N + 1)


def dfs(x):

    visit[x] = True

    for item in MAP[x]:

        if visit[item] != True:
            result[item] = x
            dfs(item)


dfs(1)

for item in result:
    if item != 0:
        print(item)
