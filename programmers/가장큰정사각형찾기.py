# https://programmers.co.kr/questions/31906
# https://small-stap.tistory.com/40
# 위 두 블로그를 보고 푼 문제입니다.


def solution(board):

    # 값 저장
    dp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    global_max = 0

    for i in range(1, len(board) + 1):
        for j in range(1, len(board[0]) + 1):

            # 이전 대각선 방향의 값이 1일경우
            # 왼쪽방향, 대각선방향, 위쪽방향에 모두 1이 존재하는 것
            if board[i - 1][j - 1] == 1:

                # 가장 작은 직사각형의 크기를 구한다.
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                # 갱신
                if dp[i][j] > global_max:
                    global_max = dp[i][j]

    return global_max**2


board = [[0, 0, 1, 1], [1, 1, 1, 1]]
