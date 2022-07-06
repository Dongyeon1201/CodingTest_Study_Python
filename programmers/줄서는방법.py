import math


def solution(n, k):

    num_list = list(range(1, n + 1))
    s = []

    while n > 0:
        unit = math.factorial(n - 1)
        q, r = divmod(k, unit)
        k = r

        if r == 0:
            s.append(num_list.pop(q - 1))
        else:
            s.append(num_list.pop(q))

        n -= 1

    return s + num_list[::-1]


print(solution(4, 14))
