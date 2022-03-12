from collections import deque

def bfs(v):
    queue = deque([v])
    count = 0

    for _ in range(N):
        v = queue.popleft()
        count += 1

        if MAP[v] == K:
            return count
        
        queue.append(MAP[v])

    return -1

N, K = map(int, input().split())

count = 0

MAP = [int(input()) for _ in range(N)]

print(bfs(0))