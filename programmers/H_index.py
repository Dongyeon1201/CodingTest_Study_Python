def solution(citations):
    answer = 0
    citations.sort(key=lambda x: -x)

    while citations[answer] >= answer and len(citations) > answer + 1:
        answer += 1

    return answer


citations = [3, 0, 6, 1, 5]
print(solution(citations))
