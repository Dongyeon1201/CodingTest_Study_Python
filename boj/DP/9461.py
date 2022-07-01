"""
F(1) = 1
F(2) = 1
F(3) = 1
F(4) = 2
F(5) = 2
F(6) = 3, F(1) + F(5)
F(7) = 4, F(2) + F(6)
F(8) = 5, F(3) + F(7)
F(9) = 7, F(4) + F(8)
F(10) = 9, F(5) + F(9)
F(11) = 12, F(6) + F(10)
F(12) = 16, F(7) + F(11)
"""


def padovan(n):

    info = [0] * 101
    info[1], info[2], info[3] = 1, 1, 1
    info[4], info[5] = 2, 2

    for i in range(6, n + 1):
        info[i] = info[i - 5] + info[i - 1]

    return info[n]


N = int(input())
for _ in range(N):
    print(padovan(int(input())))
