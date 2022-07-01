N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0] = info[0]

# Bottom-Top 방식으로 값을 구해나간다.
# 이전의 색칠한 최소 비용에 현재 비용을 더한다.
for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + info[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + info[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + info[i][2]

print(min(dp[-1]))
