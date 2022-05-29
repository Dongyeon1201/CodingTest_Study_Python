from collections import deque


def solution(people, limit):

    people = deque(sorted(people))
    answer = 0

    # 아직 보트에 타지 못한 사람들이 존재할 때
    while people:

        # 가장 무게가 높은 사람과 낮은 사람이 같이 탈 수 있을 때
        # 1대에 같이 태운다.
        if len(people) >= 2 and people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
            answer += 1

        # 제일 무거운 사람을 혼자 1대에 태운다.
        else:
            people.pop()
            answer += 1

    return answer


people = [70, 80, 50]
limit = 100
print(solution(people, limit))
