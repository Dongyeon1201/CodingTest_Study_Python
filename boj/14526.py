from collections import deque

def bfs(s, t):
    
    queue = deque([(s, t, 0)])
    visit = [False] * 1000

    while queue:
        for _ in range(len(queue)):
            v, k, count = queue.popleft()
            visit[v] = True

            if v == k:
                return count
            
            if v < k and visit[v+1] != True:
                queue.append((v+1, k, count+1))

            if v < k and visit[v*2] != True:
                queue.append((v*2, k+3, count+1))

N = int(input())
result = []

for _ in range(N):
    S, T = map(int, input().split())
    result.append(bfs(S, T))

for item in result: 
    print(item)