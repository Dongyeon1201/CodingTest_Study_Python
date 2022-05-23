def solution(citations):
    answer = 0
    citations.sort(key=lambda x: -x)

    for idx, item in enumerate(citations):
        if idx >= item:
            return idx

    return len(citations)


citations = [3, 0, 6, 1, 5]
print(solution(citations))
