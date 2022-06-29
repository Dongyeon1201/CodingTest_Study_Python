N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 최소 값 저장
min_value = float("inf")

# 스타트팀 저장(링크로 해도됨)
start_team = []

# 팀의 점수 구하기
def get_team_sum(team):

    team_sum = 0

    for i in range(len(team)):
        for j in range(i + 1, len(team)):

            # S_ij + S_ji
            team_sum += board[team[i]][team[j]] + board[team[j]][team[i]]

    return team_sum


def dfs(depth):

    global min_value

    # start_team 구성이 완료된경우
    if depth == N // 2:

        link_team = []

        # start_team에 없는 인원은 모두 link_team
        for i in range(N):
            if i not in start_team:
                link_team.append(i)

        # start_team과 link_team 점수를 비교
        start_team_score = get_team_sum(start_team)
        link_team_score = get_team_sum(link_team)

        if abs(start_team_score - link_team_score) < min_value:
            min_value = abs(start_team_score - link_team_score)

        return

    # start_team 구성
    for i in range(N):
        if i not in start_team:

            # 중복되지 않는 start_team을 구성
            # [3, 2, 1], [1, 2, 3] 와 같이 중복 방지
            # 오름차순으로만 구성되도록 만든다.
            if len(start_team) > 0 and i <= start_team[-1]:
                continue

            start_team.append(i)
            dfs(depth + 1)
            start_team.pop()


dfs(0)

print(min_value)
