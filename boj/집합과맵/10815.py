from collections import defaultdict

info = defaultdict(bool)

N = int(input())
info_a = list(map(int, input().split()))

for item in info_a:
    info[item] = True

M = int(input())
info_b = list(map(int, input().split()))

for item in info_b:
    if info[item]:
        print("1", end=" ")
    else:
        print("0", end=" ")
