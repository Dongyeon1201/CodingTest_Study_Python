# https://programmers.co.kr/learn/courses/30/lessons/68645


def solution(n):

    # 각 행을 저장하는 배열
    # 이제 모양을 피라미드가 아닌, 직각삼각형의 형태로 보면 편하다.
    answer = [[0] * i for i in range(1, n + 1)]

    # 1부터 채운다.
    num = 1

    # 행과 열 좌표
    row, column = -1, 0

    # 숫자는 아래 1~3 순서를 한번의 사이클로 반복한다.
    # 숫자가 채워지지 않은 가장 왼쪽의 (row, column)를 시작으로 진행한다.
    # 1. row를 1씩 증가하며, 숫자를 채워준다. 첫 사이클에서는 n번 반복한다.
    # 2. 가장 큰 row에서 column을 채워준다.(제일 하단 부분) 첫 사이클에서는 n-1번 반복한다. (0번 column은 1번 과정을 통해 채워짐)
    # 3. row, column을 1씩 빼주며, 위로 올라간다. 이 과정에서 숫자를 채워주며, 첫 사이클에서는 n-2번 반복한다.
    # 다음 사이클에서는 n을 n-3 값으로 갱신해준다.
    # 삼각형 모양으로 점점 안으로 들어가면서, 한 라인마다 채울 수 있는 숫자의 갯수가 1씩 감소하는것이다.
    for i in range(n, 0, -3):
        for _ in range(i):
            row += 1
            answer[row][column] = num
            num += 1
        for _ in range(i - 1):
            column += 1
            answer[row][column] = num
            num += 1
        for _ in range(i - 2):
            row -= 1
            column -= 1
            answer[row][column] = num
            num += 1

    # 2차원 배열 -> 1차원 배열
    return [item for line in answer for item in line]


print(solution(7))
