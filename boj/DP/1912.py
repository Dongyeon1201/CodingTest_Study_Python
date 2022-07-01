N = int(input())
infos = list(map(int, input().split()))
dp = [0] * N
dp[0] = infos[0]

for i in range(1, N):
    dp[i] = max(infos[i], infos[i] + dp[i - 1])

print(max(dp))
