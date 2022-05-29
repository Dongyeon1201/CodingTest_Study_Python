def solution(n, words):

    for i, item in enumerate(words):

        # 한 글자일 때
        if len(item) < 2:
            return [i % n + 1, i // n + 1]

        # 첫 순서가 아닐 때
        if i > 0:
            # 이전 단어의 마지막 글자와 현재 첫 글자가 다를 때
            if words[i - 1][-1] != item[0]:
                return [i % n + 1, i // n + 1]

            # 이전에 사용했던 단어일 때
            if item in words[:i]:
                return [i % n + 1, i // n + 1]

    # 탈락자가 없을 경우 [0, 0] 반환
    return [0, 0]


n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

print(solution(n, words))
