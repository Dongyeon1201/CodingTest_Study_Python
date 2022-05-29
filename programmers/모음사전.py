from itertools import product


def solution(word):

    info = []

    for i in range(1, 6):
        for item in product("AEIOU", repeat=i):
            info.append("".join(item))

    info.sort()

    return info.index(word) + 1


word = "AAAE"
print(solution(word))
