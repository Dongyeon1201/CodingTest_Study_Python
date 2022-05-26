# 블록을 제거 후, 사라진 블록의 갯수를 세는 함수이다.
# 세로로 밀어야하기 때문에, 행과 열을 뒤집어 구현이 편하도록 만든게 포인트이다.
def pop_num(b, m, n):

    # 사라지는 블록의 좌표를 저장하는 곳
    # 중복되는 좌표 처리를 위해 set을 사용
    pop_set = set()

    # 행과 열을 뒤집었으니, 반복도 큰 for문이 열의 갯수, 작은 for문이 행의 갯수로 맞춰야한다.
    for i in range(1, n):
        for j in range(1, m):

            # 만약 사각형의 범위의 좌표들의 값이 모두 동일하며, 비어있는 블록공간이 아닐 때
            if b[i][j] == b[i - 1][j - 1] == b[i - 1][j] == b[i][j - 1] != "_":

                # 없앨 블록의 좌표를 저장하는 set 자료형에 추가한다.
                pop_set |= set([(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)])

    # 삭제할 좌표의 목록을 조회하여, 실제 보드에 적용한다.
    # 삭제된 위치의 값은 0으로 변경
    for i, j in pop_set:
        b[i][j] = 0

    # 보드를 라인별로 조회
    for i, row in enumerate(b):

        # 빈 공간을 '_' 값으로 표시
        # 삭제된 블록만큼 빈 공간 생성
        empty = ["_"] * row.count(0)

        # 빈 공간을 라인의 시작 부분에 설정 + 빈 공간이 아닌 나머지 원소를 붙인다.
        # 해당 라인의 값 갱신
        b[i] = empty + [block for block in row if block != 0]

    # 삭제된 블록의 갯수 반환
    return len(pop_set)


def solution(m, n, board):

    count = 0

    # 기존 보드를 행과 열을 뒤집은 형태로 변경한다.
    b = list(map(list, zip(*board)))

    # 삭제된 블록이 없을 때 까지
    while True:

        # 삭제된 블록 갯수 확인
        pop = pop_num(b, m, n)

        # 삭제된 블록이 없다면
        # 지금까지 삭제된 블록의 갯수 반환
        if pop == 0:
            return count

        # 갯수에 추가
        count += pop


m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

print(solution(m, n, board))
