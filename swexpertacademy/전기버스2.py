# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do


def dfs(idx, battery_change, info):

    # 최소 충전 횟수를 저장한 변수
    global best

    # 만약 현재 충전 횟수가 이미 최소 충전 횟수를 넘어선경우 더 이상 확인 X
    if best < battery_change:
        return

    # 만약 현재 위치가 목적지에 도착한 경우 & 최소 충전 횟수보다 작거나 같을 경우
    if idx >= info[0]:

        # 최소 충전횟수 변경
        best = battery_change
        return

    # 만약 목적지가 아닌 경우, 현재 정류장의 배터리량을 확인
    count = info[idx]

    # 현재 배터리량으로 갈 수 있는 모든 정류장을 DFS로 재귀
    for i in range(count, 0, -1):
        dfs(idx + i, battery_change + 1, info)


T = int(input())
for test_case in range(1, T + 1):

    # 각 케이스마다 최소 충전 횟수를 저장할 전역변수
    best = float("inf")

    # N과 각 정류장마다 배터리 충전량을 저장한 배열
    info = list(map(int, input().split()))

    # 1번 정류장부터
    dfs(1, 0, info)

    # 첫 충전횟수는 누적하지 않기 때문에, -1을 해준다.
    print(f"#{test_case} {best-1}")
