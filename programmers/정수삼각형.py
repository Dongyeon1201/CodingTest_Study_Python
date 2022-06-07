def solution(triangle):

    # 각 라인의 최대 합계를 저장하는 리스트
    sum_info = [[0] * len(item) for item in triangle]
    X = [-1, 0]

    # 라인별로 반복
    for line in range(len(triangle)):

        # 각 라인의 가장 마지막 요소부터 역순으로 확인
        for idx in range(len(triangle[line]) - 1, -1, -1):

            # 첫 라인일 경우 별도의 연산 X
            if line == 0:
                sum_info[0][0] = triangle[0][0]
            else:
                for x in X:

                    # 현재 idx를 가르킬 수 있는 이전 라인의 인덱스 구하기
                    new_idx = idx + x

                    # 해당 라인의 범위 내 인덱스인지 확인
                    if 0 <= new_idx < len(triangle[line - 1]):

                        # 새로운 합계를 구한다.
                        new_sum = sum_info[line - 1][idx + x] + triangle[line][idx]

                        # 만약 현재 라인의 인덱스에 오기까지 가장 큰 합계일 경우
                        if new_sum > sum_info[line][idx]:
                            sum_info[line][idx] = new_sum

    # 가장 마지막 라인의 가장 큰 값
    return max(sum_info[-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
