# 참고 : https://prgms.tistory.com/101
# 참고 : https://bladejun.tistory.com/166


# 시간 T를 이분탐색으로 구하여, 해당 시간 T에서 조건에 맞게 금/은을 운반할 수 있는지 확인
# 이분탐색으로 시간을 변경하며 최소 시간을 구한다.
def solution(a, b, g, s, w, t):
    start = 0

    # 금/은 최대 필요량(1e9 * 2) * 왕복(2) * 최대 시간 사용(1e5)
    end = 10**9 * 2 * 2 * 10**5
    answer = 10**9 * 2 * 2 * 10**5

    while start <= end:
        mid = (start + end) // 2

        # 해당 시간에 운반할 수 있는 최대 금과 은의 양을 구한다.
        gold_max = 0
        silver_max = 0

        # 해당 시간에 운반할 수 있는 최대 무게를 구한다.
        weight_max = 0

        for item in zip(g, s, w, t):

            # 현재 도시의 금과 은의 양과 운반 가능 무게, 편도 시간
            gold_state, silver_state, weight_state, time_state = item

            # 운반 가능 횟수를 구한다.
            count = mid // time_state // 2

            # 마지막 1번 편도가 가능하다면 1 더해준다.
            if mid % (time_state * 2) >= time_state:
                count += 1

            # 해당 도시의 최대로 옮길 수 있는 금의 양을 누적
            gold_max += gold_state if gold_state < weight_state * count else weight_state * count

            # 해당 도시의 최대로 옮길 수 있는 은의 양을 누적
            silver_max += silver_state if silver_state < weight_state * count else weight_state * count

            # 해당 도시에서 최대로 옮길 수 있는 무게를 누적
            weight_max += gold_state + silver_state if gold_state + silver_state < weight_state * count else weight_state * count

        # 아래 조건을 만족하면, 해당 시간을 사용하면 신도시 건설에 필요한 금 a, 은 b를 모두 옮길 수 있다.
        if a <= gold_max and b <= silver_max and a + b <= weight_max:

            # 최저 시간일 경우 갱신
            answer = min(answer, mid)

            # 더 작은 시간을 탐색
            end = mid - 1

        # 만족하지 않는 경우, 더 큰 시간을 탐색
        else:
            start = mid + 1

    return answer


a = 90
b = 500
g = [70, 70, 0]
s = [0, 0, 500]
w = [100, 100, 2]
t = [4, 8, 1]

a = 10
b = 10
g = [100]
s = [100]
w = [7]
t = [10]

print(solution(a, b, g, s, w, t))
