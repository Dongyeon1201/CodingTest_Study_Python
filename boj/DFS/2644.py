import sys

input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visit = [False] * (N + 1)
is_found = False

for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(node, count):

    if node == B:
        global is_found
        is_found = True

        print(count)
        return

    if is_found == False:
        for connect in graph[node]:
            if visit[connect] == False:
                visit[connect] = True
                dfs(connect, count + 1)
                visit[connect] = False


visit[A] = True
dfs(A, 0)

if is_found == False:
    print(-1)
