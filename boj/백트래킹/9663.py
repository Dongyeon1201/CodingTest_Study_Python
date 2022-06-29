# 해당 위치에 퀸을 놓아도 되는지
def correct(row):

    # 현재행 이전까지 모든 행의 퀸을 확인
    # 현재 5행이라면, 1~4행의 이전 퀸들과 확인
    for i in range(row):

        # result[row] == result[i] : 같은 열이거나
        # abs(row - i) == abs(result[row] - result[i]) : 대각선 위치일 때
        if result[row] == result[i] or abs(row - i) == abs(result[row] - result[i]):
            return False

    # 이전의 모든 행의 퀸과 공격할 수 없을 때
    return True


# 첫행부터 마지막행까지 반복(dfs)
def dfs(row):

    # 마지막행까지 모두 적합한 위치일 때
    if row == N:
        global answer
        answer += 1
        return

    # 각 행의 퀸을 첫 행 ~ 마지막 행까지 이동하면서 확인한다.
    for i in range(N):

        if visit[i]:
            continue

        # result[row] = column
        # row행 column열에 퀸이 존재한다.
        result[row] = i

        # 다른 퀸과 겹치지 않는 적합한 위치일 때
        if correct(row):

            visit[i] = True

            # 다음 행을 확인
            dfs(row + 1)

            visit[i] = False


N = int(input())

# N개의 퀸을 각 행의 첫 위치에 놓고 시작
result = [0] * N

# 이미 해당열에 퀸이 존재하는지 확인
visit = [False] * N

# 총 방법 갯수
answer = 0

dfs(0)

print(answer)
