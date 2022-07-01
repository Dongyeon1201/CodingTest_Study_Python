N = int(input())


def fibonacci(n):

    info = [0] * 1000001

    info[1] = 1
    info[2] = 2

    for k in range(3, n + 1):
        info[k] = (info[k - 1] + info[k - 2]) % 15746

    return info[n]


print(fibonacci(N))
