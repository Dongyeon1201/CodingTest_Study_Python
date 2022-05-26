# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do


def dfs(idx, sum_cost):
    global best

    # 최소 비용보다 이미 같거나 클경우, 더이상 탐색 X
    if best <= sum_cost:
        return

    # 만약 모든 visit이 True일 경우 -> 탐색 끝 의미
    if list(set(visit)) == [True]:
        best = sum_cost

    for i in range(N):

        # 방문하지 않은 곳일경우
        if visit[i] == False:

            # 방문 설정
            visit[i] = True

            # 다음 행으로 이동, 합계 누적
            dfs(idx + 1, sum_cost + info[idx][i])

            # 같은 단계의 다른 경우 탐색을 위해, 원래대로 복구
            visit[i] = False


T = int(input())
for test_case in range(1, T + 1):
    best = float("inf")

    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    visit = [False] * N

    dfs(0, 0)

    print(f"#{test_case} {best}")
