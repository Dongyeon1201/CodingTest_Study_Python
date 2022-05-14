# 출처 : https://yensr.tistory.com/61
def solution(N, number):
    dp = [[]]

    # N을 1번 사용 ~ 8번 사용
    for i in range(1, 9):

        temp = []

        if int(str(N) * i) == number:
            return i
        else:
            temp.append(int(str(N) * i))

        # ex) N 5번 사용을 구하는 경우 -> 사칙 연산이기 때문에, 숫자의 위치에 따라 값이 변할 수 있다.
        # 따라서 전부 구한다.
        # 1번 사용 경우와 4번 이루어지는 경우 사칙연산 -> 총 5번
        # 2번 사용 경우와 3번 이루어지는 경우 사칙연산 -> 총 5번
        # 3번 사용 경우와 2번 이루어지는 경우 사칙연산 -> 총 5번
        # 4번 사용 경우와 1번 이루어지는 경우 사칙연산 -> 총 5번
        for j in range(1, i):

            # k + l이 i가 되는 경우를 전부 구한다.
            for k in dp[j]:
                for l in dp[i - j]:

                    # + 연산
                    temp.append(k + l)

                    # - 연산
                    if k - l >= 0:
                        temp.append(k - l)
                    # * 연산
                    temp.append(k * l)

                    # // 연산
                    if l != 0 and k != 0:
                        temp.append(k // l)

        # 찾는 숫자가 연산 결과 목록에 존재하는 경우
        if number in temp:
            return i

        # 전체 연산 결과에 추가
        dp.append(list(set(temp)))

    return -1
