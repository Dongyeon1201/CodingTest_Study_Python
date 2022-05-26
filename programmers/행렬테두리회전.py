def swing(rc, x1, y1, x2, y2):

    min_num = float("inf")

    # 값 임시 저장
    tmp = rc[x1][y1]

    # 왼쪽 라인은 x1+1 ~ x2 까지 행 값들을 한칸씩 위로 올린다.
    # 이때 가장 처음 원소(x1)이 사라지기 때문에, tmp에 임시로 저장한다.
    for i in range(x1, x2):
        rc[i][y1] = rc[i + 1][y1]
        if rc[i][y1] < min_num:
            min_num = rc[i][y1]

    # 아래 라인은 y1+1 ~ y2 까지 열 값들을 한칸씩 왼쪽으로 이동한다.
    for i in range(y1, y2):
        rc[x2][i] = rc[x2][i + 1]
        if rc[x2][i] < min_num:
            min_num = rc[x2][i]

    # 오른쪽 라인은 x1 ~ x2-1 까지 행 값들을 한칸씩 아래로 내린다.
    for i in range(x2, x1, -1):
        rc[i][y2] = rc[i - 1][y2]
        if rc[i][y2] < min_num:
            min_num = rc[i][y2]

    # 위쪽 라인은 y1 ~ y2-1 까지 열 값들을 한칸씩 오른쪽으로 이동한다.
    for i in range(y2, y1, -1):
        rc[x1][i] = rc[x1][i - 1]
        if rc[x1][i] < min_num:
            min_num = rc[x1][i]

    # tmp가 이동해야될 위치로 값을 설정해준다.
    rc[x1][y1 + 1] = tmp
    if rc[x1][y1 + 1] < min_num:
        min_num = rc[x1][y1 + 1]

    return min_num


def solution(rows, columns, queries):

    vector = [[columns * i + j for j in range(1, columns + 1)] for i in range(rows)]

    result = []

    for querie in queries:
        x1, y1, x2, y2 = querie
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

        result.append(swing(vector, x1, y1, x2, y2))

    return result


queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
rows = 6
columns = 8
print(solution(rows, columns, queries))
