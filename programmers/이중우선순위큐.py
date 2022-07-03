import heapq


def solution(operations):

    # 데이터가 저장되는 배열(최소힙으로 사용)
    answer = []

    for op in operations:

        # 메소드, 숫자를 각각 연산에서 얻어온다.
        method, value = op.split()

        # INSERT
        if method == "I":

            # 최소힙으로 숫자 추가
            heapq.heappush(answer, int(value))

        # DELETE
        elif method == "D":

            # 배열에 값이 존재해야한다.
            if answer:

                # 최소값 제거
                if value == "-1":

                    # 최소힙의 최상단값 제거 -> 최소값 제거
                    heapq.heappop(answer)

                # 최대값 제거
                elif value == "1":

                    # nlargest 메소드를 이용하여 최대값을 구한다.
                    max_value = heapq.nlargest(1, answer).pop()

                    # 해당 리스트에서 제거
                    answer.remove(max_value)

    # 만약 데이터가 존재할 경우
    if answer:

        # 최소값을 얻어온다.
        min_value = heapq.heappop(answer)

        # 값이 1개만 남아있을 경우 최소값과 최대값은 같다.
        # 만약 그렇지 않다면 최대값이 별도로 존재하기 때문에 구해준다.
        max_value = heapq.nlargest(1, answer).pop() if answer else min_value

        return [max_value, min_value]

    # 데이터가 존재하지 않을 경우
    else:
        return [0, 0]


operations = ["I 7", "I 5", "I -5", "D -1"]
print(solution(operations))
