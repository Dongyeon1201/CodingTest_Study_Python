from collections import deque


def solution(people, limit):

    people = deque(sorted(people))
    answer = 0

    while people:

        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
            answer += 1
        else:
            if people[0] > limit // 2:
                break
            else:
                

    return answer + len(people)


people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))
