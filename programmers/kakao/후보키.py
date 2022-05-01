from collections import defaultdict
from itertools import combinations


def solution(relation):

    answer = 0

    # row 수
    row_count = len(relation)

    # 각 row의 column 수
    column_count = len(relation[0])

    # 각 column 별로 참조 가능하도록 변경
    relation = list(zip(*relation))

    # 각 조합의 유일성이 만족하는지 사전 형태로 저장
    # 인덱스 0 -> 첫번째 컬럼
    # 인덱스 1 -> 두번째 컬럼
    # 인덱스 2 -> 세번째 컬럼
    # ...
    unique_info = defaultdict(list)

    # 1개의 컬럼 ~ 컬럼을 모두 사용했을 때의 조합 모두 확인
    for i in range(1, column_count + 1):

        # 모든 인덱스의 조합, 즉 모든 컬럼의 조합을 확인
        for item in combinations(range(column_count), i):

            # 선택된 인덱스(컬럼)의 조합을 저장
            temp = list(zip(*[relation[k] for k in item]))

            # 선택된 인덱스를 키 값으로 사용하기 위해 연결된 문자열로 변경
            # EX) (1,3,4) -> "134"
            key = "".join(map(str, item))

            # 만들어진 문자열을 키 값으로 사용하여, 유일성을 만족하는지 Boolean 값으로 저장
            unique_info[key] = len(list(set(temp))) == row_count

            # 유일성을 만족할 때
            if unique_info[key]:

                # 1개의 컬럼일 때 -> 최소성 무조건 만족
                if i == 1:
                    answer += 1

                # 2개 이상의 컬럼일 때 -> 별도의 최소성 확인 로직을 거쳐야 함
                else:
                    # 최소성을 만족하는지 확인
                    is_minimality = True

                    # 1개의 속성이 빠졌을 때 조합으로만 확인
                    # 최소성은 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미(문제에 적혀있음)
                    for minimality_item in combinations(item, len(item) - 1):

                        # 이전처럼 선택된 인덱스를 키 값으로 사용하기 위해 연결된 문자열로 변경
                        minimality_key = "".join(map(str, minimality_item))

                        # 기존의 모든 조합의 유일성을 기록했던 dict에서 해당 조합의 유일성을 만족하는지 확인
                        # 만약 하나의 속성이 빠져도 유일성을 만족하는 경우 -> 최소성 만족 X
                        if unique_info[minimality_key]:
                            is_minimality = False
                            break

                    # 최소성이 만족하는 경우만 +1
                    if is_minimality:
                        answer += 1

    return answer


# relation = [
#     ["a", "1", "aaa", "c", "ng"],
#     ["a", "1", "bbb", "e", "g"],
#     ["c", "1", "aaa", "d", "ng"],
#     ["d", "2", "bbb", "d", "ng"],
# ]

relation = [
    ["100", "ryan", "music", "2"],
    ["200", "apeach", "math", "2"],
    ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"],
    ["600", "apeach", "music", "2"],
]

print(solution(relation))
