from collections import defaultdict

N, M = map(int, input().split())
S = [input() for _ in range(N)]
strs = [input() for _ in range(M)]
info = defaultdict(bool)
answer = 0

for item in S:
    info[item] = True

for item in strs:
    if info[item]:
        answer += 1

print(answer)
