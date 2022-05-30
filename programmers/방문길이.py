from collections import defaultdict


def solution(dirs):

    state = (0, 0)
    visit = defaultdict(list)
    answer = 0

    # 이동 방향 (x, y) 좌표 저장
    arrow_info = {
        "U": (0, 1),
        "L": (-1, 0),
        "R": (1, 0),
        "D": (0, -1),
    }

    for dir in dirs:

        # 현재 좌표
        x, y = state

        # 새로운 좌표 x, y
        vx = x + arrow_info[dir][0]
        vy = y + arrow_info[dir][1]

        # 범위를 벗어나지 않는 경우
        if -5 <= vx <= 5 and -5 <= vy <= 5:

            # 이미 방문한 길이 아닌 경우
            if (x, y) not in visit[(vx, vy)]:

                answer += 1

                # 두 좌표간 방문여부를 양방향으로 기록
                visit[(vx, vy)].append((x, y))
                visit[(x, y)].append((vx, vy))

            # 현재 좌표 갱신
            state = (vx, vy)

    return answer


dirs = "ULURRDLLU"
print(solution(dirs))
