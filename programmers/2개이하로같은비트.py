# https://programmers.co.kr/learn/courses/30/lessons/77885


def solution(numbers):

    answer = []

    for number in numbers:

        # 짝수일때는 최하단 비트가 0이기 때문에, 1을 더한 다음 홀수가 조건에 맞는 답이다.
        if number % 2 == 0:
            answer.append(number + 1)

        # 홀수일 경우, 최하단부터 가장 먼저 나온 '0'비트를 찾은 후, right 비트를 1증가시킨다.
        # 여기서 가장 최하단쪽에서부터 찾는 이유는, 조건을 만족하는 숫자중 가장 작은 수가 필요하기 때문이다.
        # right 비트를 1 증가되면 해당 비트는 0으로 변하고, 자연스럽게 기존의 '0' 비트는 1로 변한다.
        # 이로써 조건에 맞게된다.
        else:
            bin_num = list("0" + format(number, "b"))

            for i in range(2, len(bin_num) + 1):
                if bin_num[-i] == "0":
                    bin_num[-i], bin_num[-i + 1] = bin_num[-i + 1], bin_num[-i]
                    break

            answer.append(int("".join(bin_num), 2))

    return answer


numbers = [2, 7]
print(solution(numbers))
