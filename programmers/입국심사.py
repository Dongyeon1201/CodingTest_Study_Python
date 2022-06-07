# # 우선 순위 큐를 이용한 풀이
# import heapq


# def solution(n, times):
#     answer = 0

#     # (시간 합, 인원)
#     check_state = [(0, len(times)), (0, len(times))]

#     while check_state:
#         sum_time, count = heapq.heappop(check_state)

#         if count == n:
#             return sum_time

#         heapq.heappush(check_state, (sum_time + 7, count + 1))
#         heapq.heappush(check_state, (sum_time + 10, count + 1))

#     return answer

# 0 ~ 최대 심사 시간 중, 최소 심사 시간을 이진 탐색을 찾는 원리
def solution(n, times):
    answer = 0

    # 최소 심사 시간 초기 값
    left = 0

    # 최대 심사 시간 초기 값
    right = n * max(times)

    while left <= right:
        count = 0
        mid = (right + left) // 2

        # 만약 심사 시간이 30 이고, 심사 구간이 A/B/C 가 존재할 때
        # 심사 가능 인원 = 30 // (A심사 시간) + 30 // (B심사 시간) + 30 // (C심사 시간)
        # 이때 구한 인원이 target(n)의 갯수와 맞춰질 때 까지 진행
        for time in times:
            count += mid // time

        if count < n:
            left = mid + 1

        # n과 동일할 때 바로 멈추지 않는 이유는, 더 짧은 심사 시간이 존재하는지 더 확인하기 때문이다.
        # 그래서 우선 answer에 넣어두고, 더 짧은 시간이 존재한다면 갱신하는 것이다.
        else:
            right = mid - 1
            answer = mid

    return answer


n = 6
times = [7, 10]
print(solution(n, times))
