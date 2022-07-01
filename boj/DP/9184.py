from collections import defaultdict

info = defaultdict(int)


def w(a, b, c):

    if info[(a, b, c)]:
        return info[(a, b, c)]

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        info[(a, b, c)] = w(20, 20, 20)

    elif a < b and b < c:
        info[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)

    else:
        info[(a, b, c)] = (
            w(a - 1, b, c)
            + w(a - 1, b - 1, c)
            + w(a - 1, b, c - 1)
            - w(a - 1, b - 1, c - 1)
        )

    return info[(a, b, c)]


while True:
    a, b, c = map(int, input().split())

    if a == b == c == -1:
        break

    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
