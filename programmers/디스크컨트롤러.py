# import heapq


# def solution(jobs):

#     # 작업을 요청 시작 시간순으로 정렬한다.
#     jobs.sort(key=lambda x: (x[1]))

#     # 가장 먼저 요청되는 작업 시간으로 설정해준다.
#     job_state = [(jobs[0][0], jobs[0][0], jobs, [])]

#     # 현재 작업 진행 상태 우선순위 큐(각 작업의 요청 ~ 종료 시간의 합을 이용한 최소힙)
#     while job_state:

#         # 지금까지의 작업 요청 ~ 종료 합, 현재 시간, 남은 작업목록
#         job_delay_sum, now_time, other_jobs, route = heapq.heappop(job_state)

#         # 남은 작업의 목록이 없을 때
#         if other_jobs == []:

#             # 지금까지의 작업 요청 ~ 종료 합을 작업의 갯수로 나눈다.
#             return job_delay_sum // len(jobs), route

#         # 남은 작업을 조회
#         for i, other_job in enumerate(other_jobs):

#             # 요청 시작 시간과 동작 시간을 조회
#             start_time, job_time = other_job

#             # 동작 가능한 작업일 때 (현재 시간 >= 요청 시작 시간)
#             if now_time >= start_time:

#                 # 기존 값에 새로운 작업의 요청 ~ 대기 시간(현재 시간 - 요청 시작 시간 + 작업 시간)을 더해준다.
#                 new_job_delay_sum = job_delay_sum + now_time - start_time + job_time

#                 # 작업의 동작 시간만큼 현재 시간을 갱신해준다.
#                 new_now_time = now_time + job_time

#                 # 최소힙에 데이터를 추가한다.
#                 heapq.heappush(
#                     job_state,
#                     (new_job_delay_sum, new_now_time, other_jobs[:i] + other_jobs[i + 1 :], route + [other_job]),
#                 )

# 풀이 참고
# https://johnyejin.tistory.com/132


from collections import deque


def solution(jobs):

    # 각 작업의 대기시간 총 합
    answer = 0

    # 현재까지 진행된 작업 시간
    now = 0

    # 전체 작업의 갯수(평균 대기시간 구하기에 활용)
    length = len(jobs)

    # 소요시간 우선 정렬 -> 그 다음으론 일찍 시작을 요청한 작업순
    jobs.sort(key=lambda x: (x[1], x[0]))

    # 수헹할 수 있는 작업들 중, 가장 작업시간이 작은 작업을 먼저 수행하는 것이다.
    while jobs:

        # 남은 모든 작업들 조회
        for i, job in enumerate(jobs):

            # 해당 작업 시작 시간이 현재 시간보다 이전이거나 동일할 경우
            if job[0] <= now:

                # 현재 시간에 작업시간 누적
                now += job[1]

                # 해당 작업의 대기시간을 총합에 누적
                answer += now - job[0]

                # 해당 작업 제외
                jobs.pop(i)

                break

        # 모든 작업을 확인후에도, 할 수 있는 작업이 없을 경우
        else:
            # 시간을 다음 시간으로 늘려준다.
            now += 1

    return answer // length


test_case = [
    ([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]], 72),
    # ([[0, 5], [2, 10], [10000, 2]], 6),
    # ([[1, 1], [2, 1], [3, 1], [5, 1]], 1),
    # ([[0, 3], [4, 4], [5, 3], [4, 1]], 3),
    # ([[0, 3], [2, 1]], 2),
]

import time

for data, correct in test_case:
    start_time = time.time()

    result = solution(data)

    print(f"USE TIME : {time.time() - start_time}")

    print(f"TEST CASE : {data}\ncorrect : {correct}\nresult : {result}")
    # print(f"ROUTE : {route}")
    print("---------------------")
