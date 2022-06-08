# 참고 : https://velog.io/@tjdud0123/%EC%9E%90%EB%AC%BC%EC%87%A0%EC%99%80-%EC%97%B4%EC%87%A0-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-python


# 행렬 출력
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end="\t")
        print("\n")


def rotate_Clockwise(matrix):
    return list(zip(*matrix[::-1]))


def solution(key, lock):

    # 열쇠 길이와 자물쇠 길이를 얻어온다.
    M, N = len(key), len(lock)

    # 가운데 자물쇠 정보가 존재하는 공간을 만든다.
    # 가장자리는 열쇠 배열이 이동하며 자물쇠와 값을 연산한다.
    board = [[0] * (M * 2 + N) for _ in range(M * 2 + N)]
    for i in range(N):
        for j in range(N):
            board[M + i][M + j] = lock[i][j]

    # key를 기본, 90도 회전, 180도 회전, 270도 회전 한번씩 모두 비교한다.
    for _ in range(4):

        # 열쇠가 존재하는 위치
        for x in range(1, M + N):
            for y in range(1, M + N):

                # 현재 열쇠가 존재하는 위치와 연산
                # 자물쇠 부분이 0 & 열쇠 부분이 1 이거나
                # 자물쇠 부분이 1 & 열쇠 부분이 0 이어야한다.
                for key_x in range(M):
                    for key_y in range(M):
                        board[x + key_x][y + key_y] ^= key[key_x][key_y]

                # 자물쇠 부분이 전부 1인지 확인
                if all(sum([board[i][M : M + N] for i in range(M, M + N)], [])):
                    return True

                # 다시 같은 구간을 XOR 하여 원상복구한다.
                for key_x in range(M):
                    for key_y in range(M):
                        board[x + key_x][y + key_y] ^= key[key_x][key_y]

        key = rotate_Clockwise(key)

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
