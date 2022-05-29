from itertools import combinations

# 두 직선의 교점 좌표를 반환
def get_point(line1, line2):
    A, B, E = line1
    C, D, F = line2

    # 두 선이 겹치거나, 교점이 없는 경우(평행)
    if (A * D) - (B * C) == 0:
        return -1

    # 교점을 반환
    else:
        x = ((B * F) - (E * D)) / ((A * D) - (B * C))
        y = ((E * C) - (A * F)) / ((A * D) - (B * C))

        # x, y 가 정수
        return (int(x), int(y)) if int(x) == x and int(y) == y else -1


def solution(line):

    # 중복되는 교점은 제거하기 위해 set 자료형 사용
    point_info = set()

    # 두 직선의 조합을 구하여 교점 얻기
    for line1, line2 in combinations(line, 2):
        point = get_point(line1, line2)

        # 교점이 존재한다면 정보 추가
        if point != -1:
            point_info.add(point)

    # 좌표들 중 가장 큰 x좌표, y좌표를 구한다.
    plus_width, plus_height = max(list(zip(*point_info))[0]), max(list(zip(*point_info))[1])

    # 좌표들 중 가장 작은 x좌표, y좌표를 구한다.
    minus_width, minus_height = min(list(zip(*point_info))[0]), min(list(zip(*point_info))[1])

    # 좌표 값을 보드에 맞게 변경하기 위해 list형태로 변경
    point_info = list(point_info)

    # 교점이 1개인 경우
    if len(point_info) < 2:
        return ["*"]

    # 각 좌표를 음 ~ 양 구간의 좌표가 아닌
    # 가장 큰 x좌표를 0으로, 가장 큰 좌표를 0으로 만들어 왼쪽 상단부터 읽을 수 있도록 만든다.
    # EX) 가장 작은 x좌표 값이 3이라면, 각 좌표를 3으로 더해준후 절대 값으로 처리하여 가장 작은 좌표에서 몇 만큼 떨어져있는지 형태로 만들어준다.
    # EX) 가장 큰 y좌표 값이 4라면, 각 좌표를 제일 큰 좌표 값으로 빼준 후 절대 값으로 처리하여 가장 큰 좌표에서 몇 만큼 떨어져있는지 형태로 만들어준다.
    for i, item in enumerate(point_info):
        x, y = item
        point_info[i] = (abs(x + minus_width), abs(y - plus_height))

    # 보드의 가로 길이 -> 가장 작은 x좌표의 절대 값 + 가장 큰 x좌표의 값 + 1(수평 축)
    # 만약 모든 교점이 같은 y축 상에 존재한다면(가장 큰 x좌표 == 가장 작은 x좌표), 보드의 가로 길이는 1이다.
    board_width = plus_width + abs(minus_width) + 1 if plus_width != minus_width else 1

    # 보드의 세로 길이 -> 가장 큰 y좌표의 값 + 가장 작은 y좌표의 절대값 + 1(수평 축)
    # 만약 모든 교점이 같은 x축 상에 존재한다면(가장 큰 y좌표 == 가장 작은 y좌표), 보드의 세로 길이는 1이다.
    board_height = plus_height + abs(minus_height) + 1 if plus_height != minus_height else 1

    # 이전에 구한 보드의 길이를 사용하여 보드를 생성
    board = [["."] * board_width for _ in range(board_height)]

    # 보드에 맞게 새롭게 변경한 좌표들을 이용하여 별을 찍어준다.
    for x, y in point_info:
        board[y][x] = "*"

    # 보드를 반환한다.
    return ["".join(item) for item in board]


line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(line))
