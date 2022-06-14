# DP 문제
def solution(m, n, puddles):

    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1

    # 물에 잠긴 곳 표시
    for x, y in puddles:
        dp[x - 1][y - 1] = -1

    # 모든 좌표 확인
    for x in range(n):
        for y in range(m):

            # 물에 잠긴 위치가 아닐 때
            if dp[x][y] != -1:

                # 현재 위치가 가장자리일 때
                if x == 0 or y == 0:

                    # 상단 가장자리일 때
                    if x == 0 and y > 0:
                        dp[x][y] = dp[x][y - 1]

                    # 좌측 가장자리일 때
                    elif y == 0 and x > 0:
                        dp[x][y] = dp[x - 1][y]

                # 가장자리 위치가 아닐 때
                # dp[x - 1][y] 와 dp[x][y - 1]가 범위 안이며, 물에 잠긴곳이 아닐때 가정
                # dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
                else:
                    if 0 <= x - 1 < n and dp[x - 1][y] != -1:
                        dp[x][y] += dp[x - 1][y]

                    if 0 <= y - 1 < m and dp[x][y - 1] != -1:
                        dp[x][y] += dp[x][y - 1]

    return dp[-1][-1] % 1000000007


m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))
