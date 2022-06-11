answer = []


# 아이디의 조합의 갯수를 얻기 위한 DFS
def dfs(info, idx, state):

    global answer

    # 마지막 행까지 탐색을 끝냈다면
    if idx >= len(info):

        # 선택된 ID의 종류를 정렬
        state.sort()

        # 이미 존재하지 않는 ID목록이라면 추가
        if state not in answer:
            answer.append(state)

        return

    # 다음 행의 이름들 중 현재 목록에 존재하지 않는 이름만 추가
    for item in info[idx]:
        if item not in state:
            dfs(info, idx + 1, state + [item])


def solution(user_id, banned_id):

    info = []
    global answer

    # 유저 목록 중복 제거
    user_id = set(user_id)

    # 각 불량 사용자 목록에 맞는 사용자를 모두 찾는다.
    for ban in banned_id:

        # 해당 불량 ID에 맞는 사용자 후보를 저장
        match = []

        # 유저 아이디를 저장
        for user in user_id:

            # 두 아이디의 길이가 다를 때 -> 확인 X
            if len(user) != len(ban):
                continue

            # 유저와 불량 사용자 아이디를 한글자씩 비교
            for user_ch, ban_ch in zip(user, ban):
                if ban_ch != "*" and user_ch != ban_ch:
                    break

            # 모든 글자가 동일할 경우 후보에 추가
            else:
                match.append(user)

        # 각 불량 사용자 아이디별로 매칭된 사용자 아이디 목록을 추가
        info.append(match)

    # dfs를 통해 종류의 갯수를 확인
    dfs(info, 0, [])

    return len(answer)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))
