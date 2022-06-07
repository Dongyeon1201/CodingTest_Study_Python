import datetime


def solution(lines):

    max_count = float("-inf")

    tasks_info = []

    for line in lines:
        line_date, line_end, line_time = line.split()

        if "." in line_time:
            line_time = datetime.datetime.strptime(line_time, "%S.%fs")
        else:
            line_time = datetime.datetime.strptime(line_time, "%Ss")

        line_end = line_date + "/" + line_end
        line_end = datetime.datetime.strptime(line_end, "%Y-%m-%d/%H:%M:%S.%f")
        line_start = line_end - datetime.timedelta(seconds=line_time.second, microseconds=line_time.microsecond - 1000)

        tasks_info.append((line_start, line_end))

    for i, item in enumerate(tasks_info):

        # 작업의 시작시간 ~ +1초 구간 카운트와 작업의 끝난시간 ~ +1초 구간의 카운트
        task_count_start = 1
        task_count_end = 1

        start, end = item

        for other_start, other_end in tasks_info[:i] + tasks_info[i + 1 :]:

            # 비교 범위보다 더 넓게 존재하는 경우
            if other_start < start - datetime.timedelta(seconds=1) and other_end > end + datetime.timedelta(seconds=1):
                task_count_start += 1
                task_count_end += 1

            else:
                # 각 작업의 시작 부분과 끝 부분을 범위내에서 비교
                # 비교 기준이 되는 작업의 시작 ~ 시작 + 1초 사이의 시간과 비교
                # 각 작업의 시작 부분과 끝 부분을 범위내에서 비교
                # 비교 기준이 되는 작업의 끝 ~ 끝 + 1초 사이의 시간과 비교
                if start <= other_start < start + datetime.timedelta(
                    seconds=1
                ) or start <= other_end < start + datetime.timedelta(seconds=1):
                    task_count_start += 1

                if end <= other_start < end + datetime.timedelta(
                    seconds=1
                ) or end <= other_end < end + datetime.timedelta(seconds=1):
                    task_count_end += 1

        if max(task_count_start, task_count_end) > max_count:
            max_count = max(task_count_start, task_count_end)

    return max_count


lines = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s",
]
# lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
print(solution(lines))
