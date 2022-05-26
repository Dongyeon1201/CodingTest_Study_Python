from itertools import permutations

# 케이스들 중 dungeons의 최대 갯수가 적기 때문에 완전탐색 사용
def solution(k, dungeons):

    # 가장 큰 카운트
    max_count = float("-inf")

    # 모든 경우의 수 확인
    for item in permutations(list(range(len(dungeons))), len(dungeons)):

        new_k = k
        temp_count = 0

        for idx in item:
            if new_k >= dungeons[idx][0]:
                new_k -= dungeons[idx][1]
                temp_count += 1

        if temp_count > max_count:
            max_count = temp_count

    return max_count


k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]

print(solution(k, dungeons))
