from collections import defaultdict


def solution(msg):

    info = defaultdict(int)
    last_num = 27
    start, idx = 0, 1
    answer = []

    for i in range(26):
        info[chr(ord("A") + i)] = i + 1

    while start < len(msg):

        while info[msg[start : idx + 1]] and idx < len(msg):
            idx += 1

        answer.append(info[msg[start:idx]])
        info[msg[start : idx + 1]] = last_num
        last_num += 1

        start = idx
        idx += 1

    return answer


msg = "KAKAO"
print(solution(msg))
