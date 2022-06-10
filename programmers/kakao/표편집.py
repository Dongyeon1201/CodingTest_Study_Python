# 참고 : https://kjhoon0330.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%91%9C-%ED%8E%B8%EC%A7%91-Python
# 각 행의 정보를 연결리스트로 저장하여 구현한 방법


def solution(n, k, cmd):

    # 현재 index 위치
    idx = k

    # 행 존재 여부
    info = ["O"] * n

    # 행 연결 정보
    table = {i: [i - 1, i + 1] for i in range(n)}

    # 삭제된 행 정보를 저장하는 스택
    stack = []

    # 첫 행
    table[0] = [None, 1]

    # 마지막 행
    table[n - 1] = [n - 2, None]

    for command in cmd:

        if command in "CZ":
            op = command
        else:
            op, value = command.split()
            value = int(value)

        if op == "C":

            # 현재 행을 삭제처리한다.
            info[idx] = "X"

            # 현재 행의 이전 행과 다음 행을 얻어온다.
            prev, next = table[idx]
            stack.append([prev, idx, next])

            ## 위치 변경
            # 마지막 행 삭제 시, 바로 직전 행으로 변경
            if next == None:
                idx = prev

            # 그 외는 다음 행으로 변경
            else:
                idx = next

            # 첫 행을 삭제한 경우 -> 다음행의 이전행 연결을 삭제
            if prev == None:
                table[next][0] = None

            # 마지막 행을 삭제한 경우 -> 이전행의 다음행 연결을 삭제
            elif next == None:
                table[prev][1] = None

            # 양쪽행의 연결을 끊어준다.
            else:
                table[prev][1] = next
                table[next][0] = prev

        elif op == "Z":

            # 최근에 삭제한 행의 정보를 얻어온다.
            prev, restore, next = stack.pop()

            # 삭제된 행을 복구한다.
            info[restore] = "O"

            # 이전 행이 존재하지 않는 행이었을 경우
            if prev == None:
                table[next][0] = restore

            # 다음 행이 존재하지 않는 행이었을 경우
            elif next == None:
                table[prev][1] = restore

            # 그 외
            else:
                table[prev][1] = restore
                table[next][0] = restore

        else:

            # UP
            if op == "U":
                for _ in range(value):
                    if table[idx][0] != None:
                        idx = table[idx][0]

            # DOWN
            elif op == "D":
                for _ in range(value):
                    if table[idx][1] != None:
                        idx = table[idx][1]

    return "".join(info)


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
print(solution(n, k, cmd))
