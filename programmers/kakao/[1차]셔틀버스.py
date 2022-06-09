from datetime import datetime, timedelta

# time 데이터 시간 추가
def time_min_add(time, min):
    return time + timedelta(minutes=min)


# time 데이터 시간 감소
def time_min_minus(time, min):
    return time - timedelta(minutes=min)


# time -> str
def convert_time_str(time):
    return datetime.strftime(time, "%H:%M")


# str -> time
def convert_str_time(time):
    return datetime.strptime(time, "%H:%M")


def solution(n, t, m, timetable):

    # 셔틀 시작시간
    shuttle_time = convert_str_time("09:00")

    # 대기자 도착 시간 오름차순으로 정렬
    timetable.sort()
    timetable = [datetime.strptime(timeitem, "%H:%M") for timeitem in timetable]

    # 셔틀 횟수만큼 반복
    for time in range(n):

        # 다음 셔틀 도착 시간
        next_shuttle_time = time_min_add(shuttle_time, t * time)

        # 셔틀 도착 전 대기중인 인원
        ready_count = 0

        # 해당 버스 시간보다 빨리 서있는 인원 구하기
        for timeitem in timetable:

            # 수용 가능 인원을 넘었을 때 종료
            if ready_count >= m:
                break

            # 셔틀을 탈 수 있는 시간에 도착한 대기자가 존재할 때
            if timeitem <= next_shuttle_time:
                ready_count += 1
            else:
                break

        # 인원이 버스 정원과 같거나 많을 경우
        if ready_count >= m:

            # 셔틀이 또 있을 경우, 셔틀 수송가능 인원만큼만 대기열에서 삭제 후, 다음버스를 확인
            if time + 1 < n:
                timetable = timetable[ready_count:]
                continue

            # 해당 인원의 가장 마지막 대기자 시간 -1분 return
            return convert_time_str(time_min_minus(timetable[:m][-1], 1))

        # 인원이 버스 정원보다 적을 경우
        else:
            # 셔틀이 또 있을 경우, 셔틀 수송가능 인원만큼만 대기열에서 삭제 후, 다음버스를 확인
            if time + 1 < n:
                timetable = timetable[ready_count:]
                continue

            # 셔틀이 없을 경우, 가장 마지막 셔틀 시간 반환
            return convert_time_str(time_min_add(shuttle_time, t * (n - 1)))


# n = 1
# t = 1
# m = 5
# timetable = ["08:00", "08:01", "08:02", "08:03"]
n, t, m, timetable = 2, 10, 2, ["09:10", "09:09", "08:00"]
print(solution(n, t, m, timetable))
